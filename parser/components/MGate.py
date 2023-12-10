from components.Node import node


class mGate(node):

    def __init__(self, Type, Type_of_Mgate, size):
        super().__init__(Type)
        self.size = size
        self.Type_of_Mgate = Type_of_Mgate
        self.G = list()
        self.output = [None]

    
    def connect_input(self, G1):
        self.G.append(G1)


    def check_input(self):
        for gate in self.G:
            if len(gate.output) == 0:
                return True
            
        return False
    

    def calculate_output(self):
        input = self.G
        if self.check_input():
            return False

        if self.Type == "Mor":
            self.output = "0"
            for i in range(len(self.G[0].output)):
                for vector in input:
                    if vector.output[i] == "1":
                        self.output = "1"
                 
        if self.Type == "Mand":
            self.output = "1"
            for i in range(len(self.G[0].output)):
                for vector in input:
                    if vector.output[i] == "0":
                        self.output = "0"
                
        
            
        return True

                
                
        
            
            