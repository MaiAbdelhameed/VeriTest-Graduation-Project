from components.Node import node


class gate(node):

    def __init__(self, Type, Type_of_gate, size):
        super().__init__(Type)
        self.size = size
        self.Type_of_gate = Type_of_gate
        self.G1 = None
        self.G2 = None
        self.output = [None] * size

        



    
    def connect_input(self, G1, G2=None): # not gates has only 1 input
        self.G1 = G1
        self.G2 = G2


    def calculate_output(self):
        if self.Type_of_gate == "not":
            if len(self.G1.output) == 0:
                return False
            else: ## not gate
                input = self.G1.output
                for i in range(0, self.size):
                    if input[i] == '1': 
                        self.output[i] = '0'
                    else:
                        self.output[i] = '1'

                    
        else:
            if len(self.G1.output) == 0 or len(self.G2.output) == 0:
                return False
            else:
                input1 = self.G1.output
                input2 = self.G2.output
                if self.Type == "and":
                    for i in range(0, self.size):
                        if input1[i] == '1' and input2[i] == '1':
                            self.output[i] = '1'
                        else:
                            self.output[i] = '0'

                if self.Type == "or":
                    for i in range(0, self.size):
                        if input1[i] == '1' or input2[i] == '1':
                            self.output[i] = '1'
                        else:
                            self.output[i] = '0'

                if self.Type == "xor":
                    for i in range(0, self.size):
                        if input1[i] == input2[i]:
                            self.output[i] = '0'
                        else:
                            self.output[i] = '1'

                if self.Type == "nand":
                    for i in range(0, self.size):
                        if input1[i] == '1' and input2[i] == '1':
                            self.output[i] = '0'
                        else:
                            self.output[i] = '1'

        return True
        
    

    def __str__(self):
        return super().__str__()


    


