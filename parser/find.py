import re


def substring_after(s, delim):
    return s.partition(delim)[2]


def get_input_output(file):
    processing_text = ""
    module_name = []
    input_name = ""
    inputs = []
    outputs2 = {}
    inputs2 = {}
    outputs = []
    bus_size = 0
    pattern = r'\[(.*?)\]'
    regex = r'\bmodule\b'
    lines = file.readlines()
    for line in lines:
        if line.startswith("//"):
            continue
        line = line.lower()
        if len(re.findall(regex,line)) != 0:
            module_name2 = ""
            processing_text = line[7:]
            for letter in processing_text:
                if letter == " ":
                    continue
                elif letter == "(":
                    break
                else:
                    module_name2+=letter
            module_name.append(module_name2)
        elif line.find("input") != -1:
            
            if line.find("]") != -1:
                input_list = substring_after(line, "]").strip("\n"
                ).strip(";").replace(" ","").split(",")
                matches = re.search(pattern, line)
                extracted_text = matches.group(1).replace(" ","").strip(";").replace("reg", "").split(":")
                if int(extracted_text[0]) != 0:
                    bus_size = int(extracted_text[0]) + 1
                else:
                    bus_size = int(extracted_text[1]) + 1

            else: # not a bus input
                input_list = substring_after(line, "input").strip("\n"
                ).strip(";").replace(" ","").replace(";","").replace("reg", "").split(",")
                bus_size = 1
            
            for i in input_list:
                inputs2.update({i.split("//")[0].replace(";","") : bus_size})

    

        elif line.find("output") != -1:
            if line.find("]") != -1:
                output_list = substring_after(line, "]").strip("\n"
                ).strip(";").replace(" ","").split(",")
                matches = re.search(pattern, line)
                extracted_text = matches.group(1).replace("reg", "").split(":")
                if int(extracted_text[0]) != 0:
                    bus_size = int(extracted_text[0]) + 1
                else:
                    bus_size = int(extracted_text[1]) + 1

            else: # not a bus output
                output_list = substring_after(line, "output").strip("\n"
                ).strip(";").replace(" ","").replace("reg", "").split(",")
                bus_size = 1
        
            
            for i in output_list:
                outputs2.update({i.split("//")[0].replace(";","")  : bus_size})


        
        elif line.find("endmodule") != -1:
            outputs.append(outputs2)
            inputs.append(inputs2)
            inputs2 = {}
            outputs2 = {}



   
    file1 = open("input_output.txt", "w")


    input_output = []
    for mod in module_name:
        list_of_inputs_outputs = []
        list_of_inputs_outputs.append(inputs[module_name.index(mod)])
        list_of_inputs_outputs.append(outputs[module_name.index(mod)])
        dictionary = {mod : list_of_inputs_outputs}
        input_output.append(dictionary)
        file1.writelines("Module Name: ")
        file1.writelines(mod)
        file1.writelines("\n")
        file1.writelines("INPUTS")
        file1.writelines("\n")
        file1.writelines("--------")
        file1.writelines("\n")
        if len(inputs[module_name.index(mod)]) != 0:
            for key, value in inputs[module_name.index(mod)].items():
                file1.writelines(key)
                file1.writelines(" ")
                file1.writelines(str(value))
                file1.writelines("\n")
        else:
            file1.writelines("NONE")
            file1.writelines("\n")



        file1.writelines("\n")
        file1.writelines("\n")

        file1.writelines("OUTPUTS")
        file1.writelines("\n")
        file1.writelines("--------")
        file1.writelines("\n")
        
        if len(outputs[module_name.index(mod)]) != 0:
            for key, value in outputs[module_name.index(mod)].items():
                file1.writelines(key)
                file1.writelines(" ")
                file1.writelines(str(value))
                file1.writelines("\n")
        else:
            file1.writelines("NONE")
            file1.writelines("\n")



        if mod != module_name[-1]:
            file1.writelines("\n")
            file1.writelines("----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
            file1.writelines("\n")
            file1.writelines("\n")
    return input_output
