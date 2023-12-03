from components.Node import node
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
        for gate in self.G:
            output = gate.output
            if len(output) == 0:
                return False
            start = gate.start
            end = gate.end
            self.output[start:end+1] = output
        if None not in self.output:
            self.output = self.output[::-1]
        return True
        
    

    def __str__(self):
        return super().__str__()


    


