from pyverilog.vparser.parser import parse
from pyverilog.vparser.ast import Width, Decl, Output, Input, Wire, Portlist



def get_assignments(node):
    assignments = []

    if isinstance(node, Decl):
        # Add the assignment to the list
        assignments.append(node)

    if isinstance(node, Portlist):
        for port in node.ports:
            if hasattr(port, "first"):
                assignments.append(port.first)
        
        

    # Recursively visit child nodes
    for child in node.children():
        assignments.extend(get_assignments(child))

    return assignments

def parse_verilog(file_path):
    # Parse the Verilog code
    ast, _ = parse([file_path])
    #ast.show()

    # Get all assignment statements from the AST
    assignments = get_assignments(ast)

    return assignments


def parse_input(assignment,input_dict, output_dict, wire_dict):
    if isinstance(assignment, Width):
        return assignment.msb.value, assignment.lsb.value
    if isinstance(assignment, Decl):
        for element in assignment.list:
            parse_input(element, input_dict, output_dict, wire_dict)
    
        
    else:
        msb=0
        lsb=0
        if assignment.width != None:
            msb, lsb = parse_input(assignment.width, input_dict, output_dict, wire_dict)
        if isinstance(assignment, Output):
            entry_dict = {assignment.name:{"msb": msb, "lsb": lsb}}
            output_dict.update(entry_dict)
        elif isinstance(assignment, Input):
            entry_dict = {assignment.name:{"msb": msb, "lsb": lsb}}
            input_dict.update(entry_dict)
        elif isinstance(assignment, Wire):
            entry_dict = {assignment.name:{"msb": msb, "lsb": lsb}}
            wire_dict.update(entry_dict) 
       
            
               


            
                   


             

def get_input_output():
    verilog_file = "module.v"
    assignments = parse_verilog(verilog_file)
    input_output_wire = list()
    input_dict = dict()
    output_dict = dict()
    wire_dict = dict()
    for dec in assignments:
        parse_input(dec, input_dict, output_dict, wire_dict)
    input_output_wire.append(input_dict)
    input_output_wire.append(output_dict)
    input_output_wire.append(wire_dict)
    return input_output_wire







