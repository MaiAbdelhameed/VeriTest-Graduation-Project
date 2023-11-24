
class gate():

    def __init__(self, Type, Type_of_gate, size):
        # super().__init__(Type)
        self.size = size
        self.Type_of_gate = Type_of_gate
        self.G1 = None
        self.G2 = None
        self.output = list()

        



    
    def connect_input(self, G1, G2=None): # not gates has only 1 input
        self.G1 = G1
        self.G2 = G2


    def calculate_output(self):
        if self.Type_of_gate == "not":
            if self.G1 == None:
                return False
            else: ## not gate
                input = self.G1.output
                for i in range(0, self.size):
                    self.output.append(not input[i])
                    
        else:
            if self.G1 == None or self.G2 == None:
                return False
            else:
                input1 = self.G1.output
                input2 = self.G2.output
                if self.Type == "AND":
                    for i in range(0, self.size):
                        if input1[i] == '1' and input2[i] == '1':
                            self.output.append('1')
                        else:
                            self.output.append('0')

                if self.Type == "OR":
                    for i in range(0, self.size):
                        if input1[i] == '1' or input2[i] == '1':
                            self.output.append('1')
                        else:
                            self.output.append('0')

        return True
        
    

    # def __str__(self):
    #     return super().__str__()


    


