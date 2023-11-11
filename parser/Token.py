class Token:

    def __init__(self, Type, name=None, start=None, end=None, size = None):
        self.Type = Type
        self.name = name
        self.start = start
        self.end = end
        self.size = size
        