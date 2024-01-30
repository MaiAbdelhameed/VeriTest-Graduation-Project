from components.Node import node
from components.output import OUTPUT

class ConstValue(node):

    def __init__(self, CONST):
        self.output = CONST
        self.connections = list()
        self.Type = "CONST"


    def process_node(self, connection): ## ConstValue is always source node
        connection.PORT = self.output
        if isinstance(connection.destination, OUTPUT):
            connection.destination.process_node(connection)
        return True
    
    def add_connection(self, connection):
        self.connections.append(connection)



    def __str__(self):
        return super().__str__()


    


