
import sys
import os
import json
import importlib


def get_generator_function(filename):
    try:
        HOME = os.environ.get('VERITEST_HOME')
        print("HOME")
        print(HOME)
        spec = importlib.util.spec_from_file_location(
            "module.name", f"{HOME}/Mode_2/Generators/{filename}")
        generator = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(generator)
        print(f"Successfully imported the generator: {filename}")
        compute_function = getattr(generator, 'compute', None)
        if compute_function is not None and callable(compute_function):
            return compute_function
        else:
            print(
                "Generator does not contain a 'compute' function or it is not callable.")

    except ModuleNotFoundError:
        print(f"generator {filename} not found or unable to import.")


def input_file_reader(file_path):
    print(f"File Path:{file_path}")
    global specs_dict
    try:
        with open(file_path, 'r') as file:
            specs_dict = json.load(file)
        return specs_dict
    except FileNotFoundError:
        print("File not found.")
        sys.exit(1)


def config_file_reader():
    global config_dict
    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.realpath(__file__))
    config_file_path = os.path.join(script_dir, 'config.json')

    try:
        with open(config_file_path, 'r') as file:
            config_dict = json.load(file)
        return config_dict
    except FileNotFoundError:
        print("Config File Not Found")
        sys.exit(1)


def main():

    # Check if arguments are provided
    if len(sys.argv) > 1:

        specs_file = sys.argv[1:][0]

    else:
        print("No command-line arguments provided please provide the specs file filename")
        sys.exit(1)

    # import config and specs files
    config_dict = config_file_reader()
    specs_dict = input_file_reader(specs_file)

    # get generator file for the category
    category = specs_dict['type']

    if category in config_dict.keys():
        print(f"category is {category}")
        compute = get_generator_function(config_dict[category])
        output_code = compute(specs_dict)

        # check if code is generated
        if (output_code == ""):
            print("Failed to generate code")
            sys.exit(1)

        # print code to file
        try:
            # configure to run from anywhere
            with open(f'uploaded_files/{specs_dict["model_name"]}.py', 'w') as file:
                for line in output_code:
                    file.write(line + '\n')
            print("specs_dict written to file successfully.")
        except IOError:
            print("Error writing to file.")

    else:
        print(
            f"No generator given for the  type {category} in the config file")
        sys.exit(1)


main()
