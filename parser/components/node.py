

class node:

    def __init__(self, Type, size=1, name=None, start=0, end=0):
        self.Type = Type
        self.size = size
        self.name = name
        self.start = start
        self.end = end

    def __str__(self):
        if self.Type == "INPUT" or self.Type == "OUTPUT":
            return self.Type + " \n \n" + self.name + "=" + str(self.size)
        
        elif self.Type == "WIRE":
            if self.start != self.end:
                return self.Type + " \n \n" + self.name  + "[" + str(self.start)+ ":" +str(self.end) +"]"
            elif self.start == self.end and self.start > 0:
                return self.Type + " \n \n" + self.name  + "[" + str(self.start) + "]"


            else:
                return self.Type + " \n \n" + self.name  + "=" + str(self.size)

    
        else:
            return self.Type
