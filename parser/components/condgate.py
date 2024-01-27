from components.Node import node
import math

class condgate(node):

    def __init__(self, condition): ## list_of_conditions is a list of tuples where tuple[0] = LHS
                                            ## while tuple[1] = RHS and tuple[2] = the conditions. 
        self.condition = condition
        self.output = list()
        self.Type = "CONDITION"
        self.G = list()
        self.size = 1
       

    def binary_to_decimal(self, string):
        decimal = 0
        for index,bit in enumerate(reversed(string)):
            decimal += int(bit) * pow(2, index)

        return decimal

            
    def connect_input(self,G1):
        self.G.append(G1)


    def calculate_output(self):
        if self.condition[0].output != None and self.condition[1].output != None:
            lhs = self.binary_to_decimal(self.condition[0].output)
            rhs = self.binary_to_decimal(self.condition[1].output)
            if self.condition[2] == "eq":
                if lhs == rhs:
                    self.output = "1"
                else:
                    self.output = "0"
            elif self.condition[2] == "gt":
                if lhs > rhs:
                    self.output = "1"
                else:
                    self.output = "0"

            elif self.condition[2] == "lt":
                if lhs < rhs:
                    self.output = "1"
                else:
                    self.output = "0"

            elif self.condition[2] == "ge":
                if lhs >= rhs:
                    self.output = "1"
                else:
                    self.output = "0"
            
            elif self.condition[2] == "le":
                if lhs <= rhs:
                    self.output = "1"
                else:
                    self.output = "0"
            
            elif self.condition[2] == "ne":
                if lhs != rhs:
                    self.output = "1"
                else:
                    self.output = "0"
            
            return True
        elif self.condition[0].output != None and self.condition[1].output == None:
            value = self.binary_to_decimal(self.condition[0].output)
            value = str(value)
            if '0' in value:
                self.output = "0"
            else: self.output = "1"
            return True
        else:
            return False

 


    def __str__(self):
        return super().__str__()


    


