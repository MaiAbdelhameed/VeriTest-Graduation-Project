

class node:

    def __init__(self, Type, size=None, name=None):
        self.Type = Type
        self.size = size
        self.name = name

    def __str__(self):
        if self.Type == "input" or self.Type == "input" or self.Type == "wire":
            return self.Type + " \n \n" + self.name + "=" + str(self.size)
    
        else:
            return self.Type
