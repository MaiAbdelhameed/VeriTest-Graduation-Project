class node:

    def __init__(self, Type):
        self.Type = Type
        

    def __str__(self):

        if self.Type == "OUTPUT" or self.Type == "INPUT" or self.Type == "WIRE":
            return self.Type + "\n \n \n" + self.name
        
        if self.Type == "CONST":
            return self.output
    
        else:
            return self.Type
        
        
