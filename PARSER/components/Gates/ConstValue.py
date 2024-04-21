from PARSER.components.Node import node
from PARSER.components.IN_OUT_WIRE.OUTPUT import OUTPUT
from PARSER.components.IN_OUT_WIRE.WIRE import wire
from PARSER.components.IN_OUT_WIRE.REG import REG

class ConstValue(node):

    def __init__(self, CONST=None, name = None):
        super().__init__("CONST")
        self.output = CONST
        self.connections = list()
        self.name = name
        


    def process_node(self, connections): ## ConstValue is always source node
        for connection in connections:
            if connection.source_range == None:
                connection.PORT = self.output
            else:
                bits = self.output[::-1]
                start = connection.source_range[0]
                end = connection.source_range[1]
                connection.PORT = bits[start:end+1][::-1]

            if isinstance(connection.destination, OUTPUT) or isinstance(connection.destination, wire) or isinstance(connection.destination, REG):
                connection.destination.add_bits_to_output(connection)

        if self.node_points_to_me(connections[0].destination.connections): 
            return False
        
        return True
    
    def node_points_to_me(self, connections):
        for connection in connections:
            if connection.destination == self:
                return True
        return False

    
    def add_connection(self, connection):
        self.connections.append(connection)



    def __str__(self):
        return super().__str__()


    


