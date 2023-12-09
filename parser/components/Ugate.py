from components.Node import node


class UGate(node):

    def __init__(self, Type, Type_of_Ugate, size):
        super().__init__(Type)
        self.size = size
        self.Type_of_Ugate = Type_of_Ugate
        self.G = list()
        self.output = [None]

    
    def connect_input(self, G1):
        self.G.append(G1)
    

    def calculate_output(self):
        input = self.G[0].output
        if len(input) == 0:
            return False

        if self.Type == "Uor":
            self.output = "0"
            for bit in input:
                if bit == "1":
                    self.output = "1"
                    break
        elif self.Type == "Uand":
            self.output = "1"
            for bit in input:
                if bit == "0":
                    self.output = "0"
                    break

        
            
        return True

                
                
        
            
            