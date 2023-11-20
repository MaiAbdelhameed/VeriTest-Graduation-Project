from node import *

class gate(node):

    def __init__(self, Type, Type_of_gate, size, start, end, name):
        super().__init__(Type)
        self.start = start
        self.end = end
        self.name = name
        self.size = size
        self.Type_of_gate = Type_of_gate
        self.G1 = None
        self.G2 = None

        



    
    def connect_input(self, G1, G2=None): # not gates has only 1 input
        self.G1 = G1
        self.G2 = G2


    def calculate_output(self):
        if self.Type_of_gate == "not":
            if self.G1 == None:
                return False
            else:
                input = self.G1.output
                for i in range(self.start, self.end, 1):
                    self.output.append(not input[i])
                    
        else:
            if self.G1 == None or self.G2 == None:
                return False
            else:
                pass # ht3ml logic kol gate hna

        

        return True
        
    

    def __str__(self):
        return super().__str__()


    


