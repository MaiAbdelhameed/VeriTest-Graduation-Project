from components.Node import node

class conditiion(node):

    def __init__(self, Type, Type_of_condition):
        super().__init__(Type)
        self.Type_of_condition = Type_of_condition
        self.G = list()
        self.output = list()
        
        

    
    def connect_input(self, cond1, cond2):
        self.G.append(cond1)
        self.G.append(cond2)
        

    def convert_to_decimal(self, string):
        string = string
        return int(string, 2)
        
    

    def calculate_output(self):
        
        input1 = self.G[0].output
        input2 = self.G[1].output
        input1 = self.convert_to_decimal(input1)
        input2 = self.convert_to_decimal(input2)
        if self.Type_of_condition == "equal":
            if input1 == input2:
                self.output = "1"
                return True
        elif self.Type_of_condition == "greaterthan":
            if input1 > input2:
                self.output = "1"
                return True
        elif self.Type_of_condition == "lessthan":
            if input1 < input2:
                self.output = "1"
                return True
        elif self.Type_of_condition == "GreaterEq":
            if input1 >= input2:
                self.output = "1"
                return True
        elif self.Type_of_condition == "LessEq":
            if input1 <= input2:
                self.output = "1"
                return True
            
        self.output = "0"
        return True

        
            


    def __str__(self):
        return super().__str__()


    


