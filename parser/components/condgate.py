from components.Node import node
import math
from components.output import OUTPUT

class condgate(node):

    def __init__(self, condition): 

        self.condition = condition
        self.Type = "CONDITION"
        self.connections = list()


    def add_connection(self, connection):
        self.connections.append(connection)
       

    def binary_to_decimal(self, string):
        decimal = 0
        for index,bit in enumerate(reversed(string)):
            decimal += int(bit) * pow(2, index)

        return decimal



    def pass_output_to_ports(self, output, connection):
        connection.PORT = output
        if isinstance(connection.destination, OUTPUT):
            connection.destination.process_node(connection)

    def process_node(self, connection):
        output = self.calc_output()
        if output == None:
            return False
        self.pass_output_to_ports(output, connection)
        return True
        
    def calc_output(self):
        list_of_conditions = list()
        output = str()
        for connection in self.connections:
            if self == connection.destination:
                list_of_conditions.append(connection.PORT)

        if len(list_of_conditions) < 2:
            lhs = list_of_conditions[0]
            rhs = ["1"] * len(lhs)
        else:
            lhs = list_of_conditions[0]
            rhs = list_of_conditions[1]
            if len(lhs) == 0 or len(rhs) == 0:
                return None
        lhs = self.binary_to_decimal(lhs)
        rhs = self.binary_to_decimal(rhs)
        if self.condition == "eq":
            if lhs == rhs:
                output = "1"
            else:
                output = "0"
        elif self.condition == "gt":
            if lhs > rhs:
                output = "1"
            else:
                output = "0"

        elif self.condition == "lt":
            if lhs < rhs:
                output = "1"
            else:
                output = "0"

        elif self.condition == "ge":
            if lhs >= rhs:
                output = "1"
            else:
                output = "0"
        
        elif self.condition == "le":
            if lhs <= rhs:
                output = "1"
            else:
                output = "0"
        
        elif self.condition == "ne":
            if lhs != rhs:
                output = "1"
            else:
                output = "0"

        return output
        
        
    

 


    def __str__(self):
        return super().__str__()


    


