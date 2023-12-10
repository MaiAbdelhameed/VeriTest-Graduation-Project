from components.Node import node


class gate(node):

    def __init__(self, Type, Type_of_gate, size):
        super().__init__(Type)
        self.size = size
        self.Type_of_gate = Type_of_gate
        self.G = list()
        self.output = [None] * size
        self.end = size -1 
        self.start = 0

        



    
    def connect_input(self, G1): # not gates has only 1 input
        self.G.append(G1)


    def calculate_output(self):
        if self.Type_of_gate == "not":
            if len(self.G[0].output) == 0:
                return False
            else: ## not gate
                input = self.G[0].output
                for i in range(self.start+1, self.end+2, 1):
                    if input[-i] == '1': 
                        self.output[-i] = '0'
                    else:
                        self.output[-i] = '1'

                    
        else:
            for gate in self.G:
                if len(gate.output) == 0:
                    return False
            else:
                if self.Type != "concat":
                    input1 = self.G[0].output
                    input2 = self.G[1].output
                    if self.Type == "and":
                        for i in range(self.start+1, self.end+2, 1):
                        
                            if input1[-i] == '1' and input2[-i] == '1':
                                self.output[-i] = '1'
                            else:
                                self.output[-i] = '0'

                    if self.Type == "or":
                        for i in range(self.start+1, self.end+2, 1):
                            if input1[-i] == '1' or input2[-i] == '1':
                                self.output[-i] = '1'
                            else:
                                self.output[-i] = '0'

                    if self.Type == "xor":
                        for i in range(self.start+1, self.end+2, 1):
                            if input1[-i] == input2[-i]:
                                self.output[-i] = '0'
                            else:
                                self.output[-i] = '1'

                    if self.Type == "nand":
                        for i in range(self.start+1, self.end+2, 1):
                            if input1[-i] == '1' and input2[-i] == '1':
                                self.output[-i] = '0'
                            else:
                                self.output[-i] = '1'
                    
                    if self.Type == "nor":
                        for i in range(self.start+1, self.end+2, 1):
                            if input1[-i] == '0' and input2[-i] == '0':
                                self.output[-i] = '1'
                            else:
                                self.output[-i] = '0'
                else:
                    finoutput = list()
                    for gate in self.G:
                        finoutput.extend(gate.output)

                    self.output = finoutput

                

        return True
        
    

    def __str__(self):
        return super().__str__()


    


