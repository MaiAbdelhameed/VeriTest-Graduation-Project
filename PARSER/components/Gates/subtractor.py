from PARSER.components.IN_OUT_WIRE.OUTPUT import OUTPUT
from PARSER.components.IN_OUT_WIRE.WIRE import wire
from PARSER.components.Node import node
from PARSER.components.IN_OUT_WIRE.REG import REG




class subtractor(node):

    def __init__(self):
        super().__init__("subtractor")
        self.connections = list()

        

    def add_connection(self,connection):
        self.connections.append(connection)


    def convert_bin_to_decimal(self, binary):
            
        
        dec = 0
        for index, bit in enumerate(binary[::-1]):
            dec += pow(2, index) * int(bit) 

        return int(dec)

    
    def calc_output(self):
        list_of_IN_port = list()
        output = list()
        for connection in self.connections:
            if self == connection.destination:
                if len(connection.PORT) == 0: return None 
                list_of_IN_port.append(list(connection.PORT))

        
        
       
        in_port_1 = list_of_IN_port[0]
        in_port_2 = list_of_IN_port[1]
       


        num1 = self.convert_bin_to_decimal(in_port_1)
        num2 = self.convert_bin_to_decimal(in_port_2)
        

        output = bin(int(num1) - int(num2))[2:]

        output2 = list()
        
        for bit in output:
            output2.append(str(bit))
    
        return output2
    

    def pass_output_to_ports(self, output, connection):
        connection.PORT = output
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
        
        if self.node_points_to_me(connections[0].destination.connections): return False ## break cycles
        return True




    
    def __str__(self):
        return super().__str__()


    


