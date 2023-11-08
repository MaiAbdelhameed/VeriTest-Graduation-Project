

class node:

    def __init__(self, Type, size, name=None):
        self.Type = Type
        self.size = size
        self.name = name

    def __str__(self):
        if self.Type == "output":
            return self.name
        else:
            return self.Type
