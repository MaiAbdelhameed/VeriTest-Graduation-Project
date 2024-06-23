from PARSER.components.IN_OUT_WIRE.OUTPUT import OUTPUT
from PARSER.components.IN_OUT_WIRE.WIRE import wire
from PARSER.components.Node import node
from PARSER.components.IN_OUT_WIRE.REG import REG




class shift(node):

    def __init__(self, Type):
        super().__init__(Type)
        self.connections = list()
        self.Type = Type

        

    def add_connection(self,connection):
        self.connections.append(connection)

    def convert_bin_to_decimal(self, binary):
            
        dec = 0
        for index, bit in enumerate(binary[::-1]):
            dec += pow(2, index) * int(bit) 

        return int(dec)


    def calc_output(self):
        shift_vector = list()
        shift_by = list()
        output = list()
        for conn in self.connections:
            if conn.destination == self:
                if len(conn.PORT) == 0: return None
                if conn.isShiftVector == True:
                    shift_vector = conn.PORT
                else:
                    shift_by = conn.PORT

        
        shift_by = self.convert_bin_to_decimal(shift_by)
        if self.Type == "shr":
            size = len(shift_vector)
            output = shift_vector[0:size-shift_by]
            output = (["0"] * abs(size-shift_by)) + output
        else:
            size = len(shift_vector)
            output = shift_vector[shift_by:]
            output = output + (["0"] * shift_by)



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


    


