class node:

    def __init__(self, Type):
        self.Type = Type
        

    def __str__(self):

        if self.Type == "OUTPUT" or self.Type == "INPUT":
            if  self.start != self.end:
                return self.Type + " \n \n" + self.name  + "[" + str(self.end)+ ":" +str(self.start) +"]" 
            elif self.start == self.end:
                return self.Type + " \n \n" + self.name  + "[" + str(self.start) + "]"
    
        elif self.Type == "WIRE":
            if self.start != self.end:
                return self.Type + " \n \n" + self.name  + "[" + str(self.end)+ ":" +str(self.start) +"]"
            elif self.start == self.end:
                return self.Type + " \n \n" + self.name  + "[" + str(self.start) + "]"

            else:
                return self.Type + " \n \n" + self.name  + "=" + str(self.size)

        elif self.Type.startswith("U"):
            return self.Type_of_Ugate
        elif self.Type == "MUX":
            return self.Type

        else:
            return self.Type_of_gate
        
        
