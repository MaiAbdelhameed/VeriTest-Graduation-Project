from PARSER.components.Node import node
# from components.GATE import gate


class OUTPUT(node):

    def __init__(self,Type, name, size, top_level, endian = "little"):
        super().__init__(Type)
        self.name = name
        self.connections = list()
        self.output = ["X"] * size
        self.size = size
        self.istoplevel = top_level
        self.endian = endian


    def add_connection(self, connection):
        self.connections.append(connection)

    def add_bits_to_output(self, connection):
        if connection.destination_range == None:
            if self.endian == "little":
                self.output = list(connection.PORT)[::-1][0:self.size][::-1]
            else:
                self.output = list(connection.PORT)[0:self.size]
            
        else:
            start = connection.destination_range[0]
            end = connection.destination_range[1]
            if self.endian == "little":
                start = self.size - start  - 1
                end = self.size - end  - 1
                indices = [i for i in range(end , start+1)]
                
                for index, value in zip(range(start, end-1, -1), reversed(connection.PORT)):
                    self.output[index] = value
                    pass   

            else:
                indices = [i for i in range(start, end+1)]
                for index, value in zip(indices, connection.PORT):
                    self.output[index] = value
                    pass
            

        
           
    def calc_output(self):
        return self.output
            
       
    
    def pass_output_to_ports(self, output, connection):
        if connection.source_range == None:
            connection.PORT = output
        else:
            start = connection.source_range[0]
            end = connection.source_range[1]
            if self.endian == "little":
                output = output[::-1]
                output = output[start:end+1]
                connection.PORT = output[::-1]
            else:
                connection.PORT = output[start:end+1]


        
        if isinstance(connection.destination, OUTPUT) or connection.destination.Type == "WIRE" or connection.destination.Type == "REG":
            connection.destination.add_bits_to_output(connection)

    

    def node_points_to_me(self, connections):
        for connection in connections:
            if connection.destination == self:
                return True
        return False

    def process_node(self, connections):
        output = self.calc_output()
        for connection in connections:
            self.pass_output_to_ports(output, connection)


        if self.node_points_to_me(connections[0].destination.connections) and "X" not in self.output: 
            return False
        
        return True
        
        
       
           

       
        
        
        


            
               
    

    def __str__(self):
        return super().__str__()


    


