import networkx as nx
from node import *
import matplotlib.pyplot as plt
import re
from find import get_input_output
import requests



def nodeingraph(G,a):
    for Nodeitr in G.nodes():
        if Nodeitr.name == a:
            return Nodeitr
    return None

def checkstack(stack):
    for item in stack:
        if item == "(":
            return True
        
    return False

def isOperator(char):

    return char == "&" or char == "^" or char == "~" or char == "~&" or char == "&~" or char == "(" or char == "|"


def whichOperator(char):

    if char == "&":
        return "and"
    elif char == "^" :
        return "xor" 
    elif char == "~":
        return "not"
    # elif char == "~&" or "&~":
    #     return "nand"
    elif char == "|":
        return "or"
    
    elif char == "(":
        return "open"
    
    elif char == ")":
        return "close"

    return ""

def shunting_yard(G, expression, output, input_output):
    flag = False ## this flag is to be triggered in case there are no parenthesis
    dictionary = input_output[0]
    values = dictionary.values()
    list_of_dicts = next(iter(values)) ## inputs and outputs of the first module (default)
    value = list_of_dicts[1]
    size_of_output = value[left]
    stack = list()
    queue = list()
    for index, char in enumerate(expression):
        if flag:
            flag = False
            continue
        if isOperator(char) and whichOperator(char) != "open" and whichOperator(char) != "close": ## hal ana opeartor 3'er parenthesis!
            ## first check if we pushed any (
            if not checkstack(stack) and expression[index+1].isalpha(): ## means there is no an open bracket
                                      ## 3ashan e7na 3ayzeen el tokens fel 7ala deh tkoon A,B,&
                queue.append(expression[index+1])
                queue.append(char)
                flag = True ## 3ashan a2dr askip next element 3ashan ana already processed it!
                continue

            else: ## lw b3dy bracket aw kan ably bracket khlas sa3etha kda el algorithm hyzbot lw7do
                stack.append(char)
       
            
        elif char == "(":
            stack.append(char)
        elif char == ")":
            while stack[-1] != "(":
                top = stack.pop()
                queue.append(top)
            if len(stack) > 0:
                stack.pop() # remove last element
                if len(stack) > 0:
                    a = stack[-1]
                    if whichOperator(a) == "not":
                        queue.append(stack.pop())


        else:
            queue.append(char)
            if (len(stack) > 0):
                if isOperator(stack[-1]): ## 3ashan lw 3ndy ~A 3ayz bs at2kd eny akhly fel queue A ~
                    if whichOperator(stack[-1]) == "not":
                        queue.append(stack.pop())
        


        
        

    while len(stack) > 0: 
        queue.append(stack.pop())

    
    '''

    converting into gates


    '''


    for char in queue:
        if isOperator(char): ## creating a gate for the expression
            Type = whichOperator(char)
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

            nodeitr = nodeingraph(G,char)
            if nodeitr == None:
                value = list_of_dicts[0]
                size = value[char]
                Node = node(Type = "input", name = char, size = size)
                stack.append(Node)

            else:
                stack.append(nodeitr)


    # we know that the top of the stack is the output for the expression

    Node = node(Type = "output", name=output, size=size_of_output)
    G.add_edge(Node, stack[-1])
        









file = open("module.txt")
file2 = open("module.txt")
lines = file.readlines()
input_output = get_input_output(file2)

G = nx.Graph()
for line in lines:


   
    if len(re.findall("assign", line)) > 0:
        splitted_text = line.split("=")
        splitted_text[0] = splitted_text[0].replace(' ','').replace("assign", "").replace("\t", "")
        splitted_text[1] = splitted_text[1].replace(' ','').replace("\t", "").replace(";","").replace("\n","")

        left = splitted_text[0]
        right = splitted_text[1]

    
        shunting_yard(G,right,left,input_output)



# for Node in G.nodes():
#     print(Node.name)
    
nx.draw_spring(G, with_labels=True)
plt.show()