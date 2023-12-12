from components.Node import node

class INPUT(node):

    def __init__(self, Type, size, start, end, name):
        super().__init__(Type)
        self.start = start
        self.end = end
        self.name = name
        self.size = size
        self.output = list()
        self.G = list()
        

    
    def connect_input(self, G1):
        self.G.append(G1)
        self.calculate_output()



    def calculate_output(self):
        self.output = self.G[0]
        return True
        
    

    def __str__(self):
        return super().__str__()


    


