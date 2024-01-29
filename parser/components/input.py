from components.Node import node

class INPUT(node):

    def __init__(self, Type, size, start, end, name):
        super().__init__(Type)
        self.start = start
        self.end = end
        self.name = name
        self.size = size
        self.connections = list()
        self.OUTPUT = [None] * size
        
    

    def add_connection(self, connection):
        self.connections.append(connection)

    
    
    def process_node(self, connection):
        if self == connection.source:
            if None not in self.OUTPUT:
                if connection.source == None:
                    connection.PORT = self.OUTPUT
                else:
                    output = self.OUTPUT[::-1]
                    start = connection.source[0]
                    end = connection.source[1]
                    connection.PORT = output[start:end+1]
                connection.destination.process_node(connection)
                return True
            else:
                return False
        else: ## Simply I will take what is connected on the port
            self.OUTPUT = connection.PORT
            
        
        


    def __str__(self):
        return super().__str__()


    


