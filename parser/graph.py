import networkx as nx
from components.node import *
from preprocessing.find import *
import matplotlib.pyplot as plt
import re
from Token import *






def nodeingraph(G,a):
    for Nodeitr in G.nodes():
        if Nodeitr.name:
            if Nodeitr.Type == "INPUT":
                if Nodeitr.name == a.name:
                    return Nodeitr

            else:
                if Nodeitr.name.replace("_WIRE", "") == a.name and a.start == Nodeitr.start and a.end == Nodeitr.end:
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

    return char.Type == "and" or char.Type == "xor" or char.Type == "not" or char.Type == "open" or char.Type == "or" or char.Type == "close"


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


def TokenwhichOperator(Token):

    return Token.Type

   

def shunting_yard(G, Tokens, output_token, Input_output_wire):
    flag = False ## this flag is to be triggered in case there are no parenthesis
    stack = list()
    queue = list()
    for index, Token in enumerate(Tokens):
        if flag:
            flag = False
            continue
        if TokenisOperator(Token) and TokenwhichOperator(Token) != "open" and TokenwhichOperator(Token) != "close": ## hal ana opeartor 3'er parenthesis!
            ## first check if we pushed any (
            if not checkstack(stack) and Tokens[index+1].name.isalpha(): ## means there is no an open bracket
                                      ## 3ashan e7na 3ayzeen el tokens fel 7ala deh tkoon A,B,&
                queue.append(Tokens[index+1])
                queue.append(Token)
                flag = True ## 3ashan a2dr askip next element 3ashan ana already processed it!
                continue

            else: ## lw b3dy bracket aw kan ably bracket khlas sa3etha kda el algorithm hyzbot lw7do
                stack.append(Token)
       
            
        elif Token.Type == "open":
            stack.append(Token)
        elif Token.Type == "close":
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
            queue.append(Token)
            if (len(stack) > 0):
                if TokenisOperator(stack[-1]): ## 3ashan lw 3ndy ~A 3ayz bs at2kd eny akhly fel queue A ~
                    if TokenwhichOperator(stack[-1]) == "not":
                        queue.append(stack.pop())
        


        
        

    while len(stack) > 0: 
        queue.append(stack.pop())

    
    '''

    converting into gates


    '''


    for Token in queue:
        if TokenisOperator(Token): ## creating a gate for the expression
            Type = TokenwhichOperator(Token)
            Node = node(Type, size = 1)
            G.add_node(Node)
            if Type != "not":
                for i in range(0,2):
                    a = stack.pop()
                    G.add_edge(a, Node)

            else:   
                a = stack.pop()
                G.add_edge(a, Node)

            stack.append(Node)
        else:    
            nodeitr = nodeingraph(G,Token)
            if nodeitr == None:
                size_of_token = Token.size 
                if Token.name in Input_output_wire[0]:
                    value = Input_output_wire[0]
                    size = value[Token.name]
                    Node = node(Type = "INPUT", name = Token.name, size = size, start = size - 1, end = 0)
                    if size_of_token == size:
                        stack.append(Node)
                        
                    else:
                        Node_WIRE = node(Type = "WIRE", name = Token.name +"_WIRE", size = abs(Token.end-Token.start)+1, start = Token.start, end = Token.end) ## abl ama tcreate node et2kd el awl feeh node wire bnfs el 7aga wla la2
                        G.add_edge(Node_WIRE,Node)
                        stack.append(Node_WIRE)

                    
                        
                elif Token.name in Input_output_wire[2]:
                    size_of_token = token.size 
                    value = Input_output_wire[2]
                    size = value[Token.name]
                    Node = node(Type = "WIRE", name = Token.name, size = size, start = size -1, end = 0)
                    if size_of_token == size:
                        stack.append(Node)
                        
                    else:
                        Node_WIRE = node(Type = "WIRE", name = Token.name + "_WIRE", size = abs(end-start)+1, start = Token.start, end = Token.end)
                        G.add_edge(Node_WIRE,Node)
                        stack.append(Node_WIRE)

            else:
                if Token.name in Input_output_wire[0]:
                    value = Input_output_wire[0]
                    size = nodeitr.size
                    size_of_token = Token.size
                    if size_of_token == size:
                        stack.append(nodeitr)
                        
                    else:
                        Node_WIRE = node(Type = "WIRE", name = Token.name + "_WIRE", size = abs(end-start) + 1, start = Token.start, end = Token.end)
                        G.add_edge(Node_WIRE,nodeitr)
                        stack.append(Node_WIRE)


                elif Token.name in Input_output_wire[2]:
                    value = Input_output_wire[2]
                    size = value[Token.name]
                    size_of_token = Token.size
                    if size_of_token == size:
                        stack.append(nodeitr)
                        
                    else:
                        Node_WIRE = node(Type = "WIRE", name = Token.name + "_WIRE", size = abs(end-start) + 1, start = Token.start, end = Token.end)
                        G.add_edge(Node_WIRE,nodeitr)
                        stack.append(Node_WIRE)
               


    # we know that the top of the stack is the output for the expression





    
    Type = "OUTPUT"
    value = Input_output_wire[1]
    out = output_token.name
    size_of_token = Token.size
    if out not in value:
        value = Input_output_wire[2]
        Type = "WIRE"






    nodeitr = nodeingraph(G,output_token)
    if nodeitr == None:
        Node = node(Type = Type, name=out, size=abs(output_token.end-output_token.start)+1, start = output_token.start, end = output_token.end)
        G.add_edge(Node, stack[-1])
        
            
         

    else:
        G.add_edge(stack[-1], nodeitr)
           
       
    

        









file = open("module.txt")
file2 = open("module.txt")
lines = file.readlines()
input_output = get_input_output(file2)
dictionary = input_output[0]
values = dictionary.values()
Input_output_wire = next(iter(values)) ## inputs and outputs of the first module (default)

G = nx.Graph()
print(Input_output_wire)
for line in lines:


   
    if len(re.findall("assign", line)) > 0:

        splitted_text = line.split("=")
        splitted_text[0] = splitted_text[0].replace(' ','').replace("assign", "").replace("\t", "")
        splitted_text[1] = splitted_text[1].replace(' ','').replace("\t", "").replace("\n","")

        out = splitted_text[0]
        right = splitted_text[1]
        Tokens = list()
        
        for index, char in enumerate(right):
            operator = whichOperator(char)
            if (char == "[" or char == "]" or char == ":" or char.isdigit() or char == ";"):
                continue
            if char.isalpha():
                start = 0
                end = 0
                if index + 1 < len(right):
                    if right[index+1] == "[":
                        regex = "(?<=" + re.escape(char) + ")\[?(\d+)(?::(\d+))?\]?"
                        matchgrp = re.findall(regex,right)
                        start = int(matchgrp[0][0])
                        end = int(matchgrp[0][1]) if len(matchgrp[0][1]) > 0 else start
                    else:
                        if char in Input_output_wire[0]:
                            value = Input_output_wire[0]
                            start = value[char] - 1
                        else:
                            value = Input_output_wire[2]
                            start = value[char] - 1


                if char in Input_output_wire[0]:
                    token = Token(Type = "INPUT", name=char, start = start, end=end, size = abs(end-start) + 1)
                elif char in Input_output_wire[1]:
                    token = Token(Type = "OUTPUT", name=char, start = start, end=end, size = abs(end-start) + 1)
                elif char in Input_output_wire[2]:
                    token = Token(Type = "WIRE", name=char, start = start, end=end, size = abs(end-start) + 1)


                    
                  
                
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
        if len(matchgrp) > 0:
            start = int(matchgrp[0][0])
            end = int(matchgrp[0][1]) if len(matchgrp[0][1]) > 0 else start

        else:
            if out2 in Input_output_wire[1]:
                value = Input_output_wire[1]
                start = value[out2] - 1
            else:
                value = Input_output_wire[2]
                start = value[out2] - 1

        output_token = Token(Type = "WIRE", name = out2, start = start, end = end, size = abs(end-start)+1)  
        shunting_yard(G,Tokens,output_token,Input_output_wire)
        tokens=""




# for Node in G.nodes():
#     print(Node.name)


# print(len(G.nodes()))
    
nx.draw_spring(G, with_labels=True)
plt.show()





