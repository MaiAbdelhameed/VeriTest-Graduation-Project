from components.Node import node
from components.Gate import gate
from components.MUX import mux

class Output(node):

    def __init__(self,Type, size, start, end, name):
        super().__init__(Type)
        self.start = start
        self.end = end
        self.name = name
        self.size = size
        self.output = [None] * size
        self.G = list()


    
    def connect_input(self, G1):
        self.G.append(G1)

    def hasNone(self):
        for bit in self.output:
            if bit == None:
                return False
        return True


    def calculate_output(self):
        for Gate in self.G:
            if isinstance(Gate, gate) or isinstance(Gate, mux) : # lw wasel ably gate 3la tool ha5od menha el output bta3ha kolo
                self.output = Gate.output
            else:
                output = Gate.output
                if len(output) == 0:
                    return False
                start = Gate.start
                end = Gate.end
                output = output[::-1]
                self.output[start:end+1] = output
                self.output = self.output[::-1]
                
        if len(self.output) != 0 and self.hasNone():
            return True
        return False
        
    

    def __str__(self):
        return super().__str__()


    


