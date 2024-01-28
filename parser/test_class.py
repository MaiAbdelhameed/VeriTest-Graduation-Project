
class test_class:

    def __init__(self, Node, start, end):
        self.Node = Node
        self.start = start
        self.end = end

    def __str__(self):
        return f"{self.Node}[{self.start}:{self.end}]"  
        