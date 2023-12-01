from components.Node import node
class Output(node):

    def __init__(self,Type, size, start, end, name):
        super().__init__(Type)
        self.start = start
        self.end = end
        self.name = name
        self.size = size
        self.output = list()
        self.G1 = None
        self.G2 = None

    
    def connect_input(self, G1):
        self.G1 = G1


    def calculate_output(self):
        self.output = self.G1.output[::-1]
        return True
        
    

    def __str__(self):
        return super().__str__()


    


