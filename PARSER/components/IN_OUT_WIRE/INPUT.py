from PARSER.components.Node import node
from PARSER.components.IN_OUT_WIRE.OUTPUT import OUTPUT
from PARSER.components.IN_OUT_WIRE.WIRE import wire
from PARSER.components.IN_OUT_WIRE.REG import REG

class INPUT(node):

    def __init__(self, Type, name, top_level, endian = "little"):
        super().__init__(Type)
        self.name = name
        self.connections = list()
        self.istoplevel = top_level
        self.endian = endian
        
    

    def add_connection(self, connection):
        self.connections.append(connection)

    def calc_output(self):
        for connection in self.connections:
            if self == connection.destination:
                if len(connection.PORT) == 0:
                    return False
                return connection.PORT

        

    

    def pass_output_to_ports(self, output, connection):
        if connection.source_range == None:
            connection.PORT = output
        else:
            start = connection.source_range[0]
            end = connection.source_range[1]
            if self.endian == "little":
                output = output[::-1]
                output = output[start:end+1]
                connection.PORT = output[::-1]
            else:
                connection.PORT = output[start:end+1]
                
        if isinstance(connection.destination, OUTPUT) or isinstance(connection.destination, wire) or isinstance(connection.destination, REG):
            connection.destination.add_bits_to_output(connection)
                

    
    def process_node(self, connections):
        output = self.calc_output()
        if output == None:
            return False
        for connection in connections:
            self.pass_output_to_ports(output, connection)


        if self.node_points_to_me(connections[0].destination.connections): 
            return False
        return True
    

    def node_points_to_me(self, connections):
        for connection in connections:
            if connection.destination == self:
                return True
        return False
            
 
        
        


    def __str__(self):
        return super().__str__()


    


