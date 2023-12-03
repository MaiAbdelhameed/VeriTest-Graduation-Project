from components.Node import node
class wire(node):

    def __init__(self, Type, size, start, end, name):
        super().__init__(Type)
        self.start = start
        self.end = end
        self.name = name
        self.size = size
        self.output = list()
        self.G1 = None
        self.G2 = None

    
    def connect_input(self, G1): ## input is a node
        self.G1 = G1


    def calculate_output(self):


        
        if self.size == len(self.G1.output):
            self.output = self.G1.output
        else:
            for i in range(self.start, self.end + 1):
                self.output.append(self.G1.output[i])

        
        return True
        
    

   


