from PARSER.components.Node import node
from PARSER.components.IN_OUT_WIRE.OUTPUT import OUTPUT
from PARSER.components.IN_OUT_WIRE.WIRE import wire
from math import pow


class Case(node):

    def __init__(self):
        super().__init__("Case")
        self.connections = list()
        self.bind = None
        self.list_of_possible_cases = list() ## for default case


    def set_list_of_possible_cases(self, list_of_possible_cases):
        self.list_of_possible_cases = list_of_possible_cases
        
    def add_connection(self, connection):
        self.connections.append(connection)

    def set_bind(self, bind):
        self.bind = bind
    
    def convert_selector_bin_to_decimal(self, binary):
        
        index = 0
        dec = 0
        for bit in binary[::-1]:
            dec += pow(2, index) * int(bit) 

        return int(dec)


        
   
    def calc_output(self):
        dict_of_in_ports = dict()
        dict_of_in_ports.update({"DEFAULT": "X"})
        selector_value = list()
        for connection in self.connections:
            if self == connection.destination:
                if connection.isSelector:
                    selector_value = connection.PORT
                else:
                    dict_of_in_ports.update({connection.port_number: connection.PORT})

        

        
        selector_value = "".join(selector_value)
        if len(selector_value) == 0:
            return None
        

        try:
            output = dict_of_in_ports[str(selector_value)]
        except:
            if selector_value not in self.list_of_possible_cases:
                output = dict_of_in_ports["DEFAULT"]
            else:
                output = "X"
            
        if len(output) > 0:
            return output
        else:
            return None
        

    def pass_output_to_ports(self, output, connection):
        if connection.source_range == None:
            connection.PORT = output
        else:
            start = connection.source_range[0]
            end = connection.source_range[1]
            connection.PORT = output[::-1][start:end+1][::-1]
        if isinstance(connection.destination, OUTPUT) or isinstance(connection.destination, wire):
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
        



        

