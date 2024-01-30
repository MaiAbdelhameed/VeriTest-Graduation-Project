from components.Node import node
from components.output import OUTPUT

class INPUT(node):

    def __init__(self, Type, size, start, end, name):
        super().__init__(Type)
        self.start = start
        self.end = end
        self.name = name
        self.size = size
        self.connections = list()
        
    

    def add_connection(self, connection):
        self.connections.append(connection)

    def calc_output(self):
        for connection in self.connections:
            if self == connection.destination:
                if len(connection.PORT) == 0:
                    return False
                return connection.PORT

        

    

    def pass_output_to_ports(self, output, connection):
        if connection.source_range == None:
            connection.PORT = output
        else:
            bits = output[::-1]
            start = connection.source_range[0]
            end = connection.source_range[1]
            connection.PORT = bits[start:end+1][::-1]
            
        if isinstance(connection.destination, OUTPUT):
            connection.destination.process_node(connection)    
                

    
    def process_node(self, connection):
        output = self.calc_output()
        if output == None:
            return False
        self.pass_output_to_ports(output, connection)
        return True
            
 
        
        


    def __str__(self):
        return super().__str__()


    


