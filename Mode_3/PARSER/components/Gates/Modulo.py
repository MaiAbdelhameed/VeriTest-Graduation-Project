from PARSER.components.IN_OUT_WIRE.OUTPUT import OUTPUT
from PARSER.components.IN_OUT_WIRE.WIRE import wire
from PARSER.components.Node import node
from PARSER.components.IN_OUT_WIRE.REG import REG
from math import floor




class Modulo(node):

    def __init__(self):
        super().__init__("Mod")
        self.connections = list()

        

    def add_connection(self,connection):
        self.connections.append(connection)


    def convert_bin_to_decimal(self, binary):
            
        
        dec = 0
        for index, bit in enumerate(binary[::-1]):
            dec += pow(2, index) * int(bit) 

        return int(dec)


    
    def calc_output(self):
        output = list()
        numerator = list()
        denominator = list()
        for connection in self.connections:
            if self == connection.destination:
                if len(connection.PORT) == 0: return None
                if connection.isNumerator == True:
                    numerator = connection.PORT
                else:
                    denominator = connection.PORT

        
        
       
        


        numerator = self.convert_bin_to_decimal(numerator)
        denominator = self.convert_bin_to_decimal(denominator)
        

        output = list(bin(int(numerator) % int(denominator))[2:])
    
        return output
    

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


    


