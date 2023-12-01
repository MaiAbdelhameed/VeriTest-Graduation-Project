from components.Node import node
class wire(node):

    def __init__(self, Type, size, start, end, name):
        super().__init__(Type)
        self.start = start
        self.end = end
        self.name = name
        self.size = size

    
    def connect_input(self, input):
        self.input = input


    def calculate_output(self):
        self.output = self.input1
        return True
        
    

   


