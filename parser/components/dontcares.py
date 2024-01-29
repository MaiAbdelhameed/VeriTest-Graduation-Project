from components.Node import node

class dontcares(node):

    def __init__(self, size):
        super().__init__("DONTCARE")
        self.size = size
        self.output = list()
        self.output = ["X"] * size
        self.type = "XXX"
        self.connections = list()

    def add_connection(self, connection):
        self.connections.append(connection)


    def __str__(self):
        return super().__str__()


    


