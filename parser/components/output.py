from components.Node import node

class OUTPUT(node):

    def __init__(self,Type, size, start, end, name, is_wire=False):
        super().__init__(Type)
        self.start = start
        self.end = end
        self.name = name
        self.size = size
        self.output = [None] * size
        self.connections = list()


    def add_connection(self, connection):
        self.connections.append(connection)

    def add_bits_to_output(self, connection):
        if connection.destination_range == None:
            self.output = connection.PORT
        else:
            start = connection.destination_range[0]
            end = connection.destination_range[1]
            size = abs(start-end)
            start = (start * -1) - 1 
            end = (start - size) - 1
            indices = [i for i, _ in enumerate(self.output)][start:end-1:-1]
            for index, value in zip(indices, reversed(connection.PORT)):
                self.output[index] = value
                pass
 

    def process_node(self, connection):
        if self == connection.source:
            pass
        else:
            self.add_bits_to_output(connection)

    

    def __str__(self):
        return super().__str__()


    


