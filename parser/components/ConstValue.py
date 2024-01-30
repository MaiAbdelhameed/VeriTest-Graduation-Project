from components.Node import node
from components.output import OUTPUT

class ConstValue(node):

    def __init__(self, CONST):
        self.output = CONST
        self.connections = list()
        self.Type = "CONST"


    def process_node(self, connections): ## ConstValue is always source node
        for connection in connections:
            connection.PORT = self.output
            if isinstance(connection.destination, OUTPUT):
                list_of_connections = list()
                list_of_connections.append(connection)
                connection.destination.process_node(list_of_connections)
        return True
    
    def add_connection(self, connection):
        self.connections.append(connection)



    def __str__(self):
        return super().__str__()


    


