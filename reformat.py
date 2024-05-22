import re


def reorder(match):
        gate_type = match.group(1)
        name = match.group(2)
        params = match.group(3).split(',')
        params = [p.strip() for p in params]  # Strip whitespace around parameters
        # Reorder parameters: out is moved to the first position
        if len(params) == 3:
            reordered_params = [params[2], params[1], params[0]]
        elif len(params) == 2:
            reordered_params = [params[1], params[0]]
        else:
            reordered_params = params
        return f'{gate_type} {name} ({", ".join(reordered_params)});'
    

def reorder_gates(file_path, output_path):
    # Read the content of the file
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Define the pattern to match AND, OR, NOT gates
    pattern = re.compile(r'(AND|OR|NOT)\s+(\S+)\s*\(\s*\.A\((\w+)\),\s*\.B\((\w+)\),\s*\.Y\((\w+)\)\s*\)\s*;')


    # Process each line and reorder the gate parameters
    modified_lines = []
    for line in lines:
        # print(line)
        ret = re.match(pattern, line)
        print(ret)
        # modified_line = pattern.sub(reorder, line)
        # modified_lines.append(modified_line)

    # Write the modified content to a new file
    with open(output_path, 'w') as file:
        file.writelines(modified_lines)

# Example usage
reorder_gates('my_module.v', 'my_module1.v')
