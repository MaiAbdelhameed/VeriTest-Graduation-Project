from components.Node import node
from components.GATE import gate
from components.MUX import mux
from components.Wire import wire
from components.ConstValue import ConstValue

class OUTPUT(node):

    def __init__(self,Type, size, start, end, name, is_wire=False):
        super().__init__(Type)
        self.start = start
        self.end = end
        self.name = name
        self.size = size
        self.output = [None] * size
        self.G = list()
        self.is_wire = True
        self.connections = list()



    def add_connection(self, connection):
        self.connections.append(connection)
    
    def connect_input(self, G1):
        self.G.append(G1)

    def hasNone(self):
        for bit in self.output:
            if bit == None:
                return False
        return True


    def calculate_output(self):
        for Gate in self.G:
            if isinstance(Gate, gate) or isinstance(Gate, mux) or isinstance(Gate, ConstValue) : # lw wasel ably gate 3la tool ha5od menha el output bta3ha kolo
                self.output = Gate.output
            elif isinstance(Gate, wire) and self.size == Gate.size:
                self.output = Gate.output
            else:
                output = Gate.output
                if len(output) == 0:
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
        
    

    def __str__(self):
        return super().__str__()


    


