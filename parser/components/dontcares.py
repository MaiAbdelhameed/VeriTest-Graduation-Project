from components.Node import node

class dontcares(node):

    def __init__(self, size):
        super().__init__("DONTCARE")
        self.size = size
        self.output = list()
        self.output = ["X"] * size
        self.type = "XXX"


    def __str__(self):
        return super().__str__()


    


