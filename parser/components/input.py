from components.Node import node

class INPUT(node):

    def __init__(self, Type, size, start, end, name):
        super().__init__(Type)
        self.start = start
        self.end = end
        self.name = name
        self.size = size
        self.connections = list()
        self.IN_ports = list()
        
    

    def add_connection(self, connection):
        self.connections.append(connection)

    
    
    def process_node(self):
        for connection in self.connections:
            if self == connection.source: ## if you source Node
                pass:



 
        
    

    def __str__(self):
        return super().__str__()


    


