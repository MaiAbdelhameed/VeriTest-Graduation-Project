
class connection:

    def __init__(self):
        self.source = None
        self.destination = None
        self.source_range = None
        self.destination_range = None
        self.isTrueValue = False
        self.isFalseValue = False
        self.isSelector = False
        self.port_number = None
        self.PORT = []

       

    def set_attr(self, source, destination, port_number = None, source_range=None, destination_range=None, isSelector = False, isTrueValue = False, isFalseValue = False):
        self.source = source
        self.destination = destination
        self.source_range = source_range
        self.destination_range = destination_range
        self.isSelector = isSelector
        self.isTrueValue = isTrueValue
        self.isFalseValue = isFalseValue
        self.port_number = port_number
        
    def __str__(self):
        if self.source_range != None and self.destination_range != None:
            if self.destination_range[0] == self.destination_range[1] and self.source_range[0] == self.source_range[1]:
                try:
                    return f"{self.destination.name}[{self.destination_range[0]}] | {self.source.name}[{self.source_range[0]}]"
                except:
                    return f"{self.destination.name}[{self.destination_range[0]}] | {self.source.Type}[{self.source_range[0]}]"
            elif self.destination_range[0] == self.destination_range[1]:
                try:
                    return f"{self.destination.name}[{self.destination_range[0]}] | {self.source.name}[{self.source_range[0]}:{self.source_range[1]}]"
                except:
                    return f"{self.destination.name}[{self.destination_range[0]}] | {self.source.Type}[{self.source_range[0]}:{self.source_range[1]}]"

            elif self.source_range[0] == self.source_range[1]:
                try:
                    return f"{self.destination.name}[{self.destination_range[0]}:{self.destination_range[1]}] | {self.source.name}[{self.source_range[0]}]"
                except:
                    return f"{self.destination.name}[{self.destination_range[0]}:{self.destination_range[1]}] | {self.source.Type}[{self.source_range[0]}]"

            else:
                try:    
                    return f"{self.destination.name}[{self.destination_range[0]}:{self.destination_range[1]}] | {self.source.name}[{self.source_range[0]}:{self.source_range[1]}]" 
                except:
                    return f"{self.destination.name}[{self.destination_range[0]}:{self.destination_range[1]}] | {self.source.Type}[{self.source_range[0]}:{self.source_range[1]}]" 
            
        elif self.source_range == None and self.destination_range != None:
            if self.destination_range[0] != self.destination_range[1]:
                return f"{self.destination.name}[{self.destination_range[0]}:{self.destination_range[1]}]" 
            else:
                return f"{self.destination.name}[{self.destination_range[0]}]"

        elif self.source_range != None and self.destination_range == None:
            if self.source_range[0] != self.source_range[1]:
                return f"{self.source.name}[{self.source_range[0]}:{self.source_range[1]}]" 
            else:
                try:
                    return f"{self.source.name}[{self.source_range[0]}]"
                except:
                    return f"{self.source_range[0]}"

        else:
            return ""
        