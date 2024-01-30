from components.Node import node


class gate(node):

    def __init__(self, Type, Type_of_gate, size):
        super().__init__(Type)
        self.size = size
        self.Type_of_gate = Type_of_gate
        self.output = [None] * size
        self.connections = list()
        self.list_of_IN_port = list()

        



    def add_connection(self,connection):
        self.connections.append(connection)


    def calc_output(self):
        in_port_1 = self.list_of_IN_port[0]
        in_port_2 = self.list_of_IN_port[1]
        output = list()
        size = len(in_port_1)
        if self.Type == "and":
            for i in range(size):
                if in_port_1[i] == '1' and in_port_2[i] == '1':
                    output.append('1')
                else:
                    output.append('0')
        elif self.Type == "or":
            for i in range(size):
                if in_port_1[i] == '1' or in_port_2[i] == '1':
                    output.append('1')
                else:
                    output.append('0')

        elif self.Type == "xor":
            for i in range(size):
                if in_port_1[i] != in_port_2[i]:
                    output.append('1')
                else:
                    output.append('0')
        return output
    

    def pass_output_to_ports(self, output):
        for connection in self.connections:
            if self == connection.source:
                connection.PORT = output
            else:
                pass
        



    def process_node(self, connection):
        if self == connection.source:
            if len(self.list_of_IN_port) != 2:
                return False
            output = self.calc_output()
            self.pass_output_to_ports(output)
            connection.destination.process_node(connection)
            return True
        else:
            self.list_of_IN_port.append(connection.PORT)



    
    def __str__(self):
        return super().__str__()


    


