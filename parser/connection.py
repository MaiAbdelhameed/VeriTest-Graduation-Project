
class connection:

    def __init__(self):
        self.source = None
        self.destination = None
        self.source_range = None
        self.destination_range = None
        self.PORT = []

    def set_attr(self, source, destination, source_range=None, destination_range=None):
        self.source = source
        self.destination = destination
        self.source_range = source_range
        self.destination_range = destination_range
        
    def __str__(self):
        if self.source_range != None and self.destination_range != None:
            return f"{self.destination.name}[{self.destination_range[0]}:{self.destination_range[1]}] | {self.source.name}[{self.source_range[0]}:{self.source_range[1]}]" 
        elif self.source_range == None and self.destination_range != None:
            return f"{self.destination.name}[{self.destination_range[0]}:{self.destination_range[1]}]" 

        elif self.source_range != None and self.destination_range == None:
            return f"{self.source.name}[{self.source_range[0]}:{self.source_range[1]}]" 

        else:
            return ""
        