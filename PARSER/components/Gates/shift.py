from PARSER.components.IN_OUT_WIRE.OUTPUT import OUTPUT
from PARSER.components.IN_OUT_WIRE.WIRE import wire
from PARSER.components.Node import node




class shift(node):

    def __init__(self, Type):
        super().__init__(Type)
        self.connections = list()

        

    def add_connection(self,connection):
        self.connections.append(connection)


    def calc_output(self):
        pass

    def pass_output_to_ports(self, output, connection):
        connection.PORT = output
        if isinstance(connection.destination, OUTPUT) or isinstance(connection.destination, wire):
            connection.destination.add_bits_to_output(connection)
        

    def node_points_to_me(self, connections):
        for connection in connections:
            if connection.destination == self:
                return True
        return False

    def process_node(self, connections):
        output = self.calc_output()
        if output == None: return False
        for connection in connections: 
            self.pass_output_to_ports(output, connection)
        
        if self.node_points_to_me(connections[0].destination.connections): return False ## break cycles
        return True




    
    def __str__(self):
        return super().__str__()


    


