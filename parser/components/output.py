from components.Node import node
from components.Gate import gate
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


    def calculate_output(self):
        for Gate in self.G:
            if isinstance(Gate, gate): # lw wasel ably gate 3la tool ha5od menha el output bta3ha kolo
                self.output = Gate.output
            else:
                output = Gate.output
                if len(output) == 0:
                    return False
                start = Gate.start
                end = Gate.end
                self.output[start:end+1] = output
                
        if None not in self.output:
            self.output = self.output[::-1]
            return True
        return False
        
    

    def __str__(self):
        return super().__str__()


    


