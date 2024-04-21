from PARSER.components.IN_OUT_WIRE.OUTPUT import OUTPUT
from PARSER.components.IN_OUT_WIRE.WIRE import wire
from PARSER.components.Node import node




class Lgate(node):

    def __init__(self, Type):
        super().__init__(Type)
        self.connections = list()

        

    def add_connection(self,connection):
        self.connections.append(connection)

    
    def calc_output(self):
        list_of_IN_port = list()
        output = list()
        for connection in self.connections:
            if self == connection.destination:
                if len(connection.PORT) == 0: return None 
                list_of_IN_port.append(list(connection.PORT))

        
        
       
        in_port_1 = list_of_IN_port[0]
        in_port_2 = list_of_IN_port[1]
        size = len(in_port_1) 

        if self.Type == "Land":
            for i in range(size):
                if in_port_1[i] == '1' and in_port_2[i] == '1':
                    output.append('1')
                else:
                    output.append('0')

        #################################################################################
        elif self.Type == "Lor":
            for i in range(size):
                if in_port_1[i] == '1' or in_port_2[i] == '1':
                    output.append('1')
                else:
                    output.append('0')
        
        if self.Type == "Lor":
            out  = '0'  
            for bit in output:
                if bit == '1':
                    out = '1'
            return out
        
        if self.Type == "Land": 
            out = '1' 
            for bit in output:
                if bit == '0':
                    out = '0'
            return out
      
    

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


    


