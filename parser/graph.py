
import networkx as nx
from components.Gate import gate
from components.INPUT import Input

from components.Wire import wire
from components.OUTPUT import Output

from preprocessing.find import *
import matplotlib.pyplot as plt
import re
from Token import *



def nodeingraph(G,a):
    for Nodeitr in G.nodes():
        if not isinstance(Nodeitr, gate):
            if Nodeitr.name == a.name:
                return Nodeitr
            if isinstance(Nodeitr, Input):
                if Nodeitr.name == a.name:
                    return Nodeitr

            elif isinstance(Nodeitr, wire):
                if Nodeitr.name == a.name:
                    return Nodeitr
                
            elif isinstance(Nodeitr, Output):
                if Nodeitr.name == a.name:
                    return Nodeitr
    return None


def checkstack(Tokens):
    for token in Tokens:
        if token.Type == "open":
            return True
        
    return False

def isOperator(char):

    return char == "&" or char == "^" or char == "~" or char == "~&" or char == "&~" or char == "(" or char == "|"

def TokenisOperator(char):

    return char.Type == "and" or char.Type == "xor" or char.Type == "not" or char.Type == "open" or char.Type == "or" or char.Type == "close" or char.Type == "nand"


def whichOperator(char):

    if char == "&":
        return "and"
    elif char == "^" :
        return "xor" 
    elif char == "~":
        return "not"
    elif char == "|":
        return "or"
    elif char == "(":
        return "open"
    elif char == ")":
        return "close"

    return ""


def TokenwhichOperator(token):

    return token.Type

   

def shunting_yard(G, Tokens, output_token, Input_output_wire, set_of_inputs, set_of_outputs):
    flag = False ## this flag is to be triggered in case there are no parenthesis
    stack = list()
    queue = list()
    for index, token in enumerate(Tokens):
        if flag:
            flag = False
            continue
        if TokenisOperator(token) and TokenwhichOperator(token) != "open" and TokenwhichOperator(token) != "close": ## hal ana opeartor 3'er parenthesis!
            ## first check if we pushed any (
            if not checkstack(stack) and Tokens[index+1].name.isalpha(): ## means there is no an open bracket
                                      ## 3ashan e7na 3ayzeen el tokens fel 7ala deh tkoon A,B,&
                queue.append(Tokens[index+1])
                queue.append(token)
                flag = True ## 3ashan a2dr askip next element 3ashan ana already processed it!
                continue

            else: ## lw b3dy bracket aw kan ably bracket khlas sa3etha kda el algorithm hyzbot lw7do
                stack.append(token)
       
            
        elif token.Type == "open":
            stack.append(token)
        elif token.Type == "close":
            while stack[-1].Type != "open":
                top = stack.pop()
                queue.append(top)
            if len(stack) > 0:
                stack.pop() # remove last element
                if len(stack) > 0:
                    a = stack[-1]
                    if TokenwhichOperator(a) == "not":
                        queue.append(stack.pop())


        else:
            queue.append(token)
            if (len(stack) > 0):
                if TokenisOperator(stack[-1]): ## 3ashan lw 3ndy ~A 3ayz bs at2kd eny akhly fel queue A ~
                    if TokenwhichOperator(stack[-1]) == "not":
                        queue.append(stack.pop())
        


        
        

    while len(stack) > 0: 
        queue.append(stack.pop())

    
    '''

    converting into gates

    
    '''
 
    
    #rabna yostor 


    

    #queue A B & C |
    for token in queue:
        if TokenisOperator(token): ## creating a gate for the expression
            Type = TokenwhichOperator(token)
            size = stack[-1].size
            Gate = gate(Type, Type, size)
            G.add_node(Gate)
            if Type != "not":
                for _ in range(0,2):
                    a = stack.pop()
                    G.add_edge(a, Gate)
                    if Gate.G1 == None:
                        Gate.G1 = a
                    else:
                        Gate.G2 = a



            else:   
                a = stack.pop()
                G.add_edge(a, Gate)
                Gate.G1 = a

            
            stack.append(Gate)
        else:    
            nodeitr = nodeingraph(G,token)
            if nodeitr == None:
                size_of_token = token.size 
                if token.name in Input_output_wire[0]:
                    value = Input_output_wire[0]
                    size = value[token.name]
                    Node = Input(Type = "INPUT", size = size, start = 0, end = size - 1, name = token.name)
                    set_of_inputs.add(Node)
                    if size_of_token == size:
                        stack.append(Node)
                    
                    else:
                        Node_WIRE = wire(Type = "WIRE", name = token.name +"_WIRE", size = abs(token.end-token.start)+1, start = token.start, end = token.end) ## abl ama tcreate node et2kd el awl feeh node wire bnfs el 7aga wla la2
                        Node_WIRE.connect_input(Node)
                        G.add_edge(Node_WIRE,Node)
                        stack.append(Node_WIRE)

                    
                        
                elif token.name in Input_output_wire[2]:
                    size_of_token = token.size 
                    value = Input_output_wire[2]
                    size = value[token.name]
                    Node = wire(Type = "WIRE", name = token.name, size = size, start = 0, end = size -1)
                    if size_of_token == size:
                        stack.append(Node)
                        
                    else:
                        Node_WIRE = wire(Type = "WIRE", name = token.name + "_WIRE", size = abs(token.end-token.start)+1, start = token.start, end = token.end)
                        Node_WIRE.connect_input(Node)
                        G.add_edge(Node_WIRE,Node)
                        stack.append(Node_WIRE)

            else:
                if token.name in Input_output_wire[0]:
                    value = Input_output_wire[0]
                    size = nodeitr.size
                    size_of_token = token.size
                    if size_of_token == size:
                        stack.append(nodeitr)
                        
                    else:
                        Node_WIRE = wire(Type = "WIRE", name = token.name + "_WIRE", size = abs(token.end-token.start) + 1, start = token.start, end = token.end)
                        Node_WIRE.connect_input(nodeitr)
                        G.add_edge(Node_WIRE,nodeitr)
                        stack.append(Node_WIRE)


                elif token.name in Input_output_wire[2]:
                    value = Input_output_wire[2]
                    size = value[token.name]
                    size_of_token = token.size
                    if size_of_token == size:
                        stack.append(nodeitr)
                        
                    else:
                        Node_WIRE = wire(Type = "WIRE", name = token.name + "_WIRE", size = abs(token.end-token.start) + 1, start = token.start, end = token.end)
                        Node_WIRE.connect_input(nodeitr)
                        G.add_edge(Node_WIRE,nodeitr)
                        stack.append(Node_WIRE)
               


    # we know that the top of the stack is the output for the expression



    
    Type = output_token.Type
    value = Input_output_wire[1]
    out = output_token.name
    size_of_token = token.size
    size_of_output = 0
    if out not in value:
        value = Input_output_wire[2]
        Type = "WIRE"
        size_of_output = value[out]
    else:
        value = Input_output_wire[1]
        size_of_output = value[out]



    nodeitr = nodeingraph(G,output_token)
    if nodeitr == None:
        Node = None
        if Type == "OUTPUT":
            Node = Output(name=out,Type = "OUTPUT", size=size_of_output, start = 0, end = size_of_output-1)
            
        else:
            Node = wire(name=out,Type = "WIRE", size=size_of_output, start = 0, end = size_of_output-1)
        
        set_of_outputs.add(Node)
        if size_of_token == size_of_output:
            Node.connect_input(stack[-1])
            G.add_edge(Node, stack[-1])
        else:
            Node_WIRE = wire(Type = "WIRE", name = output_token.name + "_WIRE", size = abs(output_token.end-output_token.start)+1, start = output_token.start, end = output_token.end)
            Node.connect_input(Node_WIRE)
            Node_WIRE.connect_input(stack[-1])
            G.add_edge(Node, Node_WIRE)
            G.add_edge(Node_WIRE, stack[-1])

            
         

    else:
        if size_of_token == size_of_output:
            nodeitr.connect_input(stack[-1])
            G.add_edge(nodeitr, stack[-1])
        else:
            Node_WIRE = wire(Type = "WIRE", name = output_token.name + "_WIRE", size = abs(output_token.end-output_token.start)+1, start = output_token.start, end = output_token.end)
            nodeitr.connect_input(Node_WIRE)
            Node_WIRE.connect_input(stack[-1])
            G.add_edge(nodeitr, Node_WIRE)
            G.add_edge(Node_WIRE, stack[-1])


    return
           
       


def parse():
    file = open("module.txt")
    file2 = open("module.txt")
    lines = file.readlines()
    input_output = get_input_output(file2)
    dictionary = input_output[0]
    values = dictionary.values()
    Input_output_wire = next(iter(values)) ## inputs and outputs of the first module (default)

    G = nx.Graph()
    set_of_inputs = set()
    set_of_outputs = set()
    for line in lines:

        line = line.lower()
        if len(re.findall("assign", line)) > 0:
            splitted_text = line.split("=")
            splitted_text[0] = splitted_text[0].replace(' ','').replace("assign", "").replace("\t", "")
            splitted_text[1] = splitted_text[1].replace(' ','').replace("\t", "").replace("\n","")
            out = splitted_text[0]
            right = splitted_text[1]
            Tokens = list()
            flag = False
            for index, char in enumerate(right):
                if (char == "[" or char == "]" or char == ":" or char.isdigit() or char == ";" or flag == True):
                    flag = False
                    continue
                if char.isalpha():
                    start = 0
                    end = 0
                    if index + 1 < len(right):
                        if right[index+1] == "[":
                            regex = "(?<=" + re.escape(char) + ")\[?(\d+)(?::(\d+))?\]?"
                            matchgrp = re.findall(regex,right)
                            end = int(matchgrp[0][0])
                            start = int(matchgrp[0][1]) if len(matchgrp[0][1]) > 0 else end
                        else:
                            if char in Input_output_wire[0]:
                                value = Input_output_wire[0]
                                end = value[char] - 1
                            else:
                                value = Input_output_wire[2]
                                end = value[char] - 1


                    if char in Input_output_wire[0]:
                        token = Token(Type = "INPUT", name=char, start = start, end=end, size = abs(end-start) + 1)
                    elif char in Input_output_wire[1]:
                        token = Token(Type = "OUTPUT", name=char, start = start, end=end, size = abs(end-start) + 1)
                    elif char in Input_output_wire[2]:
                        token = Token(Type = "WIRE", name=char, start = start, end=end, size = abs(end-start) + 1)


                        
                    
                    
                else:
                    if whichOperator(char) == "not":
                        if index + 1 < len(right):
                            next_operator = whichOperator(right[index + 1])
                            if next_operator == "and":
                                flag = True
                                Type = "nand"
                                token = Token(Type=Type, name="1")
                            else:
                                Type = whichOperator(char)
                                token = Token(Type=Type, name="1")


            
                Tokens.append(token)


            out2 = out.replace(' ','').replace("\t", "").replace("[","").replace("]","").replace(":","")
            out2  = re.sub(r'\d', '', out2)
            regex = "(?<=" + re.escape(out2) + ")\[?(\d+)(?::(\d+))?\]?"
            matchgrp = re.findall(regex,out)
            start = 0
            end = 0
            
            if out2 in Input_output_wire[1]:
                out_token = "OUTPUT"
            else:
                out_token = "WIRE"

            if len(matchgrp) > 0:
                end = int(matchgrp[0][0])
                start = int(matchgrp[0][1]) if len(matchgrp[0][1]) > 0 else end

            else:
                if out2 in Input_output_wire[1]:
                    value = Input_output_wire[1]
                    end = value[out2] - 1
                else:
                    value = Input_output_wire[2]
                    end = value[out2] - 1



            output_token = Token(Type = out_token, name = out2, start = start, end = end, size = abs(end-start)+1)  
            shunting_yard(G,Tokens,output_token,Input_output_wire, set_of_inputs, set_of_outputs)
            token = None
            Tokens = list()

    # nx.draw_spring(G, with_labels = True)
    # plt.show()
    return G, set_of_inputs, set_of_outputs     





    





