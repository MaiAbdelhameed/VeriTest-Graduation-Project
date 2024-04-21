
import matplotlib.pyplot as plt
from Coverage.random_stimuli import random_stimuli
import networkx as nx
from pyverilog.vparser.ast import *
import re
sys.path.append("..")
from PARSER.graph import parse_verilog






class My_Block:
    def __init__(self, block_id):
        self.block_id = block_id
        self.statements_list = []
        self.blocks_list = []
        # self.type = type
        self.cond = []

    def __str__(self):
        # Convert the list of tuples to a string representation
        statements_str = "\n".join(str(statement)
                                   for statement in self.statements_list)

        # Convert the list of block objects to a string representation
        objects_str = "\n".join(str(obj.block_id) for obj in self.blocks_list)

        # Construct the complete string representation of the block
        block_str = f"Block ID: {self.block_id}\nCondition: {self.cond}\nStatements List:\n{statements_str}\nObjects List:\n{objects_str}"

        return block_str


id = 1
flowbreak_statements = [IfStatement, CaseStatement, Repeat,
                        ForStatement, DelayStatement, Disable, TaskCall, FunctionCall]
flag = False
flag2 = False


def parse_blocks(obj, G, parent=None, conditions=None):
    global id  # Declare id as global to modify it within the function
    global flag
    global flag2
    if obj is None:
        return None

    if isinstance(obj, Block):
        block = My_Block(block_id=id)
        id += 1  # Increment id
        block.cond = conditions
        flag = False
        for x in obj.statements:
            # Pass current block as parent
            a = parse_blocks(x, G, parent=block)
            if a is None:
                if flag2 is False:
                    block.statements_list.append(
                        (str(x.left.var) + '=' + str(x.right.var), x.lineno))
                else:
                    if block.blocks_list and isinstance(block.blocks_list[-1], My_Block):
                        # Access the statements_list attribute of the last My_Block object in blocks_list
                        block.blocks_list[-1].statements_list.append(
                            (str(x.left.var) + '=' + str(x.right.var), x.lineno))
        return block

    elif isinstance(obj, NonblockingSubstitution) or isinstance(obj, BlockingSubstitution):
        if flag is True:
            block = My_Block(block_id=id)
            block.cond = conditions
            block.statements_list.append(
                (str(obj.left.var) + '=' + str(obj.right.var), obj.left.lineno))
            id += 1  # Increment id
            flag = False
            flag2 = True
            G.add_node(block)  # Add node for the My_Block object
            if parent is not None:
                G.add_edge(parent, block)  # Add edge from parent to block
                parent.blocks_list.append(block)
            return block
        else:
            return None

    elif isinstance(obj, IfStatement):
        flag = True
        flag2 = False
        if obj.false_statement is None:
            if conditions is None:
                conditions = []
            conditions.append((1, obj.cond))
            true_block = parse_blocks(
                obj.true_statement, G, parent, conditions[:])
            flag = True
            G.add_node(true_block)  # Add node for true block
            if parent is not None:
                # Add edge from parent to true block
                G.add_edge(parent, true_block)
            return true_block
        else:
            if conditions is None:
                conditions = []
            conditions.append((1, obj.cond))
            true_block = parse_blocks(
                obj.true_statement, G, parent, conditions[:])
            flag = True
            flag2 = False
            conditions[-1] = (0, obj.cond)
            false_block = parse_blocks(
                obj.false_statement, G, parent, conditions[:])
            flag = True
            flag2 = False
            if true_block is not None:
                G.add_node(true_block)  # Add node for true block
                if parent is not None:
                    # Add edge from parent to true block
                    G.add_edge(parent, true_block)
                    if true_block not in parent.blocks_list:
                        parent.blocks_list.append(true_block)
            if false_block is not None:
                if isinstance(false_block, tuple):  # handles if else if instances
                    blocks = (true_block,)
                    for item in false_block:
                        G.add_node(item)
                        blocks + (item,)
                        if parent is not None:
                            # Add edge from parent to false block
                            G.add_edge(parent, item)
                    return blocks
                else:
                    G.add_node(false_block)  # Add node for false block
                    if parent is not None:
                        # Add edge from parent to false block
                        G.add_edge(parent, false_block)
            # Return only one block for IfStatement
            return (true_block, false_block)

    elif isinstance(obj, CaseStatement):
        all_conditions = []
        flag = True
        flag2 = False
        for case in obj.caselist:
            if case.cond is None:
                block = parse_blocks(case.statement, G, parent, all_conditions)
                flag = True
                flag2 = False
            else:
                all_conditions.append((0, case.cond, str(obj.comp)))
                if isinstance(case.statement, CaseStatement) or isinstance(case.statement, IfStatement):
                    new_parent = My_Block(block_id=id)
                    new_parent.cond = [(1, case.cond, str(obj.comp))]
                    id += 1  # Increment id
                    G.add_node(new_parent)  # Add node for true block
                    if parent is not None:
                        # Add edge from parent to block
                        G.add_edge(parent, new_parent)
                        if new_parent not in parent.blocks_list:
                            parent.blocks_list.append(new_parent)
                    parse_blocks(case.statement, G, new_parent)
                    flag = True
                    flag2 = False
                else:
                    block = parse_blocks(case.statement, G, parent, [
                                         (1, case.cond, str(obj.comp))])
                    flag = True
                    flag2 = False
                    if block is not None:
                        G.add_node(block)  # Add node for true block
                        if parent is not None:
                            # Add edge from parent to block
                            G.add_edge(parent, block)
                            if block not in parent.blocks_list:
                                parent.blocks_list.append(block)
        return block


def parse_verilog_constant(verilog_const_str):
    # Split the string at the single quote character
    parts = verilog_const_str.split("'")
    if len(parts) == 1:
        return int(parts[0])  # since default in verilog is decimal
    elif len(parts) != 2:
        raise ValueError("Invalid Verilog constant format")

    # Extract the width and base
    width = int(parts[0])
    base = parts[1][0]

    # Extract the value
    value_str = parts[1][1:]
    if base == 'b':
        return int(value_str, 2)
    elif base == 'h':
        return int(value_str, 16)
    elif base == 'd':
        return int(value_str)
    else:
        raise ValueError("Unsupported base in Verilog constant")

# Function to evaluate a Pyverilog AST node representing a Verilog condition


def evaluate_condition(cond, comp, input_values):

    if isinstance(cond, Partselect):
        msb = int(cond.msb.value)
        lsb = int(cond.lsb.value)
        size = msb - lsb + 1
        input_string = input_values[str(cond.var)][0]
        reversed_msb = len(input_string) - 1 - msb
        reversed_lsb = len(input_string) - 1 - lsb
        new_Str = str(size) + "'b" + \
            input_string[reversed_msb:reversed_lsb + 1]
        return parse_verilog_constant(new_Str)

    elif isinstance(cond, Pointer):
        bit = int(cond.ptr.value)
        input_string = input_values[str(cond.var)][0]
        new_bit = len(input_string) - 1 - bit
        new_Str = "1'b" + input_string[new_bit]
        return parse_verilog_constant(new_Str)

    elif isinstance(cond, Identifier):
        # Base case: Operand is an identifier (input variable)
        # Retrieve the value of the input variable from input_values dictionary
        return parse_verilog_constant(input_values[cond.name][0])

    elif isinstance(cond, IntConst):
        # Base case: Operand is an integer constant
        return parse_verilog_constant(cond.value)

    # Case statements
    elif isinstance(cond, tuple) and (len(cond) == 1):
        # Base case: Operand is an integer constant
        return parse_verilog_constant(input_values[comp][0]) == parse_verilog_constant(str(cond[0]))

    elif isinstance(cond, Operator):
        # Recursive case: Operand is an operator node (e.g., GreaterThan, Eq, Lor, Land)
        # Evaluate the left and right sub-expressions recursively
        left_result = evaluate_condition(cond.left, comp, input_values)
        right_result = evaluate_condition(cond.right, comp, input_values)

        # Perform the operation based on the operator type
        operator_type = cond.__class__.__name__
        if operator_type == 'GreaterThan':
            return left_result > right_result
        elif operator_type == 'GreaterEq':
            return left_result >= right_result
        elif operator_type == 'LessThan':
            return left_result < right_result
        elif operator_type == 'LessEq':
            return left_result <= right_result
        elif operator_type == 'Eq':
            return left_result == right_result
        elif operator_type == 'NotEq':
            return left_result != right_result
        elif operator_type == 'Land':
            return left_result and right_result
        elif operator_type == 'Lor':
            return left_result or right_result
        elif operator_type == 'LNot':
            return not right_result
        else:
            return False
        # Add more cases for other operators as needed


# input_test_cases = {'sel': 3}  # Input test case values

# ---------------


def get_root(G):
    root = next(node for node, degree in G.in_degree() if degree == 0)
    return root


def block_coverage(G, TOP_LEVEL_ENTITY):
    statements_covered = []
    input_test_cases = random_stimuli(
        1, TOP_LEVEL_ENTITY)  # HEREEEE give stuff to mark

    def traverse(node, explore):
        # Evaluate the condition using the input test cases
        if node.cond is not None:
            final_result = True
            if explore:
                for condition in node.cond:
                    if len(condition) == 3:
                        result = evaluate_condition(
                            condition[1], condition[2], input_test_cases)
                    else:
                        result = evaluate_condition(
                            condition[1], None, input_test_cases)
                    if condition[0] == 0:  # else statements so condition is inverted
                        result = not result
                    final_result = final_result and result
            else:
                final_result = False
        else:
            final_result = True  # Block has no condition

        print("Block ID: ", node.block_id,
              " Condition result:", final_result, "\n")

        if final_result is True:  # If the block is covered then mark its statements as covered
            statements_covered.extend(node.statements_list)
            # Traverse children only if the final result is True
            for child in G.successors(node):
                traverse(child, explore=True)
        else:
            for child in G.successors(node):
                traverse(child, explore=False)
        return

    root = get_root(G)
    traverse(root, explore=True)
    print("Statements Covered: ", statements_covered)


def remove_delay_control(file):
    # Read file
    with open(file, 'r') as f:
        content = f.read()

    # Delay control regex pattern # then any number of digits then either ; or not followed by whitespaces
    pattern = r'#(\d+)(;?\s*)'

    # Substitute found matches with empty string
    modification = re.sub(pattern, '', content)

    # Write the modification to the given file
    with open(file, 'w') as f:
        f.write(modification)


def COVERAGE_MAIN(TOP_LEVEL_ENTITY):
    # Remove delay control statements
    remove_delay_control(TOP_LEVEL_ENTITY)
    G = nx.DiGraph()  # Use DiGraph for directed graph
    _, always, _ = parse_verilog(TOP_LEVEL_ENTITY)
    if (len(always) > 1):
        root_block = My_Block(block_id=0)
        G.add_node(root_block)
        for always_block in always:  # 0 w 1...etc.
            x = parse_blocks(always_block.statement, G)
            # root_block = parse_blocks(always[0].statement, G)
            root_block.blocks_list.append(x)
            G.add_node(x)  # Add the block as a node in the graph
            G.add_edge(root_block, x)
    else:
        x = parse_blocks(always[0].statement, G)
        G.add_node(x)

    pos = nx.circular_layout(G)
    # pos = nx.shell_layout(G)

    nx.draw(G, pos, with_labels=True, node_size=5000,
            node_color='skyblue', font_size=12)
    plt.show()

    block_coverage(G, TOP_LEVEL_ENTITY)
    pass
