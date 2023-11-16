

class node:

    def __init__(self, Type, size=1, name=None, start=0, end=0):
        self.Type = Type
        self.size = size
        self.name = name
        self.start = start
        self.end = end

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

    
        else:
            return self.Type
        
        return "aaaa"
