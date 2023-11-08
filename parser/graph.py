import networkx as nx
from node import *
import matplotlib.pyplot as plt
import re



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

def shunting_yard(G, expression, output, size):
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
            Node = node(Type = char, name = char, size = 1)
            stack.append(Node)


    # we know that the top of the stack is the output for the expression

    Node = node(Type = "output", name=output, size=1)
    G.add_edge(Node, stack[-1])
        







text = "F = ((A & B) | C ) ^ D"


regex = r"(?<=\=).*"
text = re.findall(regex,text)[0]
print(text)
text = text.replace(" ","")


G = nx.Graph()
shunting_yard(G,text,"F",1)

nx.draw_spring(G, with_labels=True)
plt.show()

















