import networkx as nx
from node import *
import matplotlib.pyplot as plt
import re
from find import get_input_output
import requests



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

    return ""

def shunting_yard(G, expression, output, input_output):


    dictionary = input_output[0]
    values = dictionary.values()
    list_of_dicts = next(iter(values)) ## inputs and outputs of the first module (default)
    value = list_of_dicts[1]
    size_of_output = value[left]
    stack = list()
    queue = list()
    for char in expression:
        if isOperator(char):
            stack.append(char)
        elif char == ")":
            while stack[-1] != "(":
                top = stack.pop()
                queue.append(top)
            if len(stack) > 0:
                stack.pop() # remove last element


        else:
            queue.append(char)


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
            while len(stack) > 0:
                a = stack.pop()
                G.add_edge(a, Node)

            stack.append(Node)
        else:
            value = list_of_dicts[0]
            size = value[char]
            Node = node(Type = "input", name = char, size = size)
            stack.append(Node)


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

nx.draw_spring(G, with_labels=True)
plt.show()

















