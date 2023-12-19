class node:

    def __init__(self, Type):
        self.Type = Type
        

    def __str__(self):

        if self.Type == "OUTPUT" or self.Type == "INPUT":
            if  self.start != self.end:
                if self.size == (self.end - self.start) + 1:
                    return self.Type + " \n \n" + self.name 
                else:
                    return self.Type + " \n \n" + self.name  + "[" + str(self.end)+ ":" +str(self.start) +"]" 
            elif self.start == self.end:
                if self.size == 1:
                     return self.Type + " \n \n" + self.name 
                else:
                    return self.Type + " \n \n" + self.name  + "[" + str(self.start) + "]"
    
        elif self.Type == "WIRE":
            if self.start != self.end:
                return self.Type + " \n \n" + self.name  + "[" + str(self.end)+ ":" +str(self.start) +"]"
            elif self.start == self.end:
                return self.Type + " \n \n" + self.name  + "[" + str(self.start) + "]"

            else:
                return self.Type + " \n \n" + self.name  + "=" + str(self.size)

        else:
            return self.Type
        
        
