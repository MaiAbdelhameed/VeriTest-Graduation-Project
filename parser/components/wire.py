from components.Node import node
from components.MUX import mux
from components.ConstValue import ConstValue
from components.Gate import gate
class wire(node):

    def __init__(self, Type, size, start, end, name, isleft=False):
        super().__init__(Type)
        self.start = start
        self.end = end
        self.name = name
        self.size = size
        self.output = [None] * size
        self.G = list()
        self.isleft = isleft
       

    
    def connect_input(self, G1): ## input is a node
        self.G.append(G1)

    def hasNone(self):
        for bit in self.output:
            if bit == None:
                return False
        return True



    def calculate_output(self):

        if self.isleft == False:
            # if self.size == len(self.output):
            #     return True
            
            if self.size == len(self.G[0].output):
                self.output = self.G[0].output
            else:
                
                
                start = self.start
                end = self.end

                # print(self, start, end, len(self.G[0].output))
                
                self.output = []
                for i in range(start + 1, end + 2, 1):
                    self.output.append(self.G[0].output[-i])
                self.output = self.output[::-1]

            
            return True
        else:
            for Gate in self.G:
                if isinstance(Gate, gate) or isinstance(Gate, mux) or isinstance(Gate, ConstValue) : # lw wasel ably gate 3la tool ha5od menha el output bta3ha kolo
                    self.output = Gate.output
                elif isinstance(Gate, wire) and self.size == Gate.size:
                    self.output = Gate.output
                else:
                    output = Gate.output
                    if len(output) == 0 or Gate.hasNone() == False:
                        return False
                    start = Gate.start
                    end = Gate.end
                    output = output[::-1]
                    # print(output)
                    # print(self, self.start, self.end)
                    self.output[start:end+1] = output
                    
                    
                    
            if len(self.output) != 0 and self.hasNone():
                return True
            return False
        
        
    

   


