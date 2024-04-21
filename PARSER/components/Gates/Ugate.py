from PARSER.components.Node import node
from PARSER.components.IN_OUT_WIRE.OUTPUT import OUTPUT
from PARSER.components.IN_OUT_WIRE.WIRE import wire
import re


class UGate(node):

    def __init__(self, Type):
        super().__init__(Type)
        self.connections = list()

    

    def add_connection(self, connection):
        self.connections.append(connection)


    def process_node(self, connections):
        output = self.calc_output()
        if output == None:
            return False
        for connection in connections:
            self.pass_output_to_ports(output, connection)
        return True
    

    def pass_output_to_ports(self, output, connection):
        connection.PORT = "".join(output)
        if isinstance(connection.destination, OUTPUT) or isinstance(connection.destination, wire):
            connection.destination.add_bits_to_output(connection)
            
    def node_points_to_me(self, connections):
        for connection in connections:
            if connection.destination == self:
                return True
        return False
    
    def calc_output(self):
        PORT = self.connections[0].PORT
        output = list()
        if len(PORT) == 0: return None

        if self.Type == "Uor":
            output = "0"
            for bit in PORT:
                if bit == "1":
                    output = "1"
                    break
        elif self.Type == "Uand":
            output = "1"
            for bit in PORT:
                if bit == "0":
                    output = "0"
                    break

        elif self.Type == "Unand":
            ones = re.findall('1', PORT)
            if len(ones) % 2 == 0:
                output = '0'
            else:
                output = '1'

        elif self.Type == "Unor":
            ones = re.findall('1', PORT)
            if len(ones) % 2 == 0:
                output = '1'
            else:
                output = '0'
        
        elif self.Type == "Uxor":
            ones = re.findall('1', PORT)
            if len(ones) % 2 == 0:
                output = '0'
            else:
                output = '1'

        elif self.Type == "Uxnor":
            ones = re.findall('1', PORT)
            if len(ones) % 2 == 0:
                output = '1'
            else:
                output = '0'

        elif self.Type == "Unot":
            for bit in PORT:
                if bit == "0": output.append("1")
                else: output.append("0")
                    
        elif self.Type == "Ulnot":
            output.append("1")
            for bit in PORT:
                if bit == "1":
                    output[0] = "0"
                    break
            
            
                    
                    
                    
                    

        return output
            
                

                
                
        
            
            