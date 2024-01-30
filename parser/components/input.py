from components.Node import node

class INPUT(node):

    def __init__(self, Type, size, start, end, name):
        super().__init__(Type)
        self.start = start
        self.end = end
        self.name = name
        self.size = size
        self.connections = list()
        self.IN_port = list()
        
    

    def add_connection(self, connection):
        self.connections.append(connection)

    

    def pass_output_to_ports(self, output):
        for connection in self.connections:
            if self == connection.source:
                if connection.source_range == None:
                    connection.PORT = output
                else:
                    bits = output[::-1]
                    start = connection.source_range[0]
                    end = connection.source_range[1]
                    connection.PORT = bits[start:end+1][::-1]
            else:
                pass        
                

    
    def process_node(self, connection):
        if self == connection.source:
            if len(self.IN_port) == 0:
                return False
            IN_port = self.IN_port
            self.pass_output_to_ports(IN_port)
            connection.destination.process_node(connection)
            return True
            
            
            
        else: 
            self.IN_port = connection.PORT
            
        
        


    def __str__(self):
        return super().__str__()


    


