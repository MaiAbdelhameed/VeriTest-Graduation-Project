import networkx as nx
from components.node import *
from preprocessing.find import *
import matplotlib.pyplot as plt
import re
from Token import *






def nodeingraph(G,a):
    for Nodeitr in G.nodes():
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
                if Token.name in Input_output_wire[0]:
                    value = Input_output_wire[0] ## we will create a new node and it's for an input
                    size = value[Token.name]
                    Node = node(Type = "INPUT", name = Token.name, size = size)
                    stack.append(Node)
                elif Token.name in Input_output_wire[2]:
                    value = Input_output_wire[2] ## we will create a new node and it's for an WIRE
                    size = value[Token.name]
                    Node = node(Type = "WIRE", name = Token.name, size = size)
                    stack.append(Node)

            else:
                stack.append(nodeitr)


    # we know that the top of the stack is the output for the expression


    Type = "OUTPUT"
    value = Input_output_wire[1]
    if out not in value:
        value = Input_output_wire[2]
        Type = "WIRE"
    size_of_out = value[out]


    nodeitr = nodeingraph(G,output_token)
    if nodeitr == None:
        Node = node(Type = Type, name=out, size=size_of_out)
        G.add_edge(Node, stack[-1])

    else:
        G.add_edge(nodeitr, stack[-1])

        









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
        splitted_text[1] = splitted_text[1].replace(' ','').replace("\t", "").replace(";","").replace("\n","")

        out = splitted_text[0]
        right = splitted_text[1]
        Tokens = list()
        output_token = Token(Type = "WIRE", name = out, start = 0, end = 0)
        for char in right:
            operator = whichOperator(char)
            if char.isalpha():
                if char in Input_output_wire[0]:
                    token = Token(Type = "INPUT", name=char, start = 0, end=0)
                elif char in Input_output_wire[1]:
                    token = Token(Type = "OUTPUT", name=char, start = 0, end=0)
                elif char in Input_output_wire[2]:
                    token = Token(Type = "WIRE", name=char, start = 0, end=0)
                
            else:
                Type = whichOperator(char)
                token = Token(Type=Type, name="1")

            Tokens.append(token)


    
        shunting_yard(G,Tokens,output_token,Input_output_wire)
        tokens=""



for Node in G.nodes():
    print(Node.name)


print(len(G.nodes()))
    
nx.draw_spring(G, with_labels=True)
plt.show()