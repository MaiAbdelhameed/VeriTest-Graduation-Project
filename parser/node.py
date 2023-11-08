

class node:

    def __init__(self, Type, size, name=None):
        self.Type = Type
        self.size = size
        self.name = name

    def __str__(self):
        if self.Type == "input":
            return self.Type + " \n \n" + self.name + "=" + str(self.size)
        
        elif self.Type == "output":
            return self.Type + " \n \n" + self.name + "=" + str(self.size)
        else:
            return self.Type
