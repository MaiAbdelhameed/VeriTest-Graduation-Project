from components.Node import node

class mux(node):

    def __init__(self, Type, start, end, size):
        super().__init__(Type)
        self.G = list()
        self.output = [None] * size
        self.selector = None
        self.start = start
        self.end = end
        self.size = size
        self.bind = None
        self.connections = list()


    def add_connection(self, connection):
        self.connections.append(connection)
   
    
    def calculate_output(self):
        for gate in self.G:
            if len(gate.output) ==  0 or len(self.selector.output) == 0:
                return False
        if self.selector.output[0] == "1":
            self.output = self.G[0].output
        else:
            self.output = self.G[1].output

        return True

        

