from components.Node import node
class wire(node):

    def __init__(self, Type, size, start, end, name):
        super().__init__(Type)
        self.start = start
        self.end = end
        self.name = name
        self.size = size
        self.output = list()
        self.G = list()
       

    
    def connect_input(self, G1): ## input is a node
        self.G.append(G1)


    def calculate_output(self):

        if self.size == len(self.output):
            return True
        
        if self.size == len(self.G[0].output):
            self.output = self.G[0].output
        else:
            
            
            start = self.start
            end = self.end

            #print(self, start, end, len(self.G[0].output))
            
            for i in range(start + 1, end + 2, 1):
                self.output.append(self.G[0].output[-i])
            self.output = self.output[::-1]

        
        return True
        
    

   


