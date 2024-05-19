from PARSER.components.Node import node
from PARSER.components.IN_OUT_WIRE.OUTPUT import OUTPUT
from PARSER.components.IN_OUT_WIRE.WIRE import wire
from PARSER.components.IN_OUT_WIRE.INPUT import INPUT
from PARSER.components.IN_OUT_WIRE.REG import REG


class Lconcatenation(node):

    def __init__(self):
        super().__init__("LCONCAT")
        self.connections = list()


    def has_any_empty_ports(self):
        for connection in self.connections:
            if self == connection.destination and len(connection.PORT) == 0: return True
        return False
    

    def add_connection(self, connection):
        self.connections.append(connection)
    
    def get_ports(self):
        dict_of_ports = dict()
        for connection in self.connections:
            if self == connection.destination: dict_of_ports.update({connection.port_number:connection.PORT})
        return dict_of_ports
    
    def calc_output(self):
        IN_PORT = None
        output = list()
        if self.has_any_empty_ports(): return None
        for connection in self.connections:
            if self == connection.destination:
                IN_PORT = connection.PORT


        
        

        return IN_PORT
    
    def pass_output_to_ports(self, output, connection):
        if connection.source_range == None:
            connection.PORT = output
        else:
            start = connection.source_range[0]
            end = connection.source_range[1]
            connection.PORT = output[::-1][start:end+1][::-1]

        if isinstance(connection.destination, OUTPUT) or isinstance(connection.destination, wire) or isinstance(connection.destination, REG):
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
        if self.node_points_to_me(connections[0].destination.connections): ## break cycles
            return False
        
        return True
            
        
            
        
   