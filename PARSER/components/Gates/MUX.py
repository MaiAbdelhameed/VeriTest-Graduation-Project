from PARSER.components.Node import node
from PARSER.components.IN_OUT_WIRE.OUTPUT import OUTPUT
from PARSER.components.IN_OUT_WIRE.WIRE import wire
from PARSER.components.IN_OUT_WIRE.REG import REG

class mux(node):

    def __init__(self):
        super().__init__("MUX")
        self.connections = list()
        self.bind = None


    def add_connection(self, connection):
        self.connections.append(connection)

    def set_bind(self, bind):
        self.bind = bind
        
   
    def calc_output(self):
        true_value = list()
        false_value = list()
        selector_value = str()
        for connection in self.connections:
            if self == connection.destination:
                if connection.isTrueValue:
                    true_value = connection.PORT
                elif connection.isFalseValue:
                    false_value = connection.PORT
                else:
                    selector_value = connection.PORT

        
        if (len(true_value) == 0 and len(false_value) == 0)  or len(selector_value) == 0:
            return None

        if selector_value[0] == "0":
            if len(false_value) > 0:
                return false_value
            else:
                return None
        
        if len(true_value) > 0:
                return true_value
        else:
            return None
        

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
        if output == None:
            return False
        for connection in connections:
            self.pass_output_to_ports(output, connection)


        if self.node_points_to_me(connections[0].destination.connections): 
            return False
        return True
        



        

