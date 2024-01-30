from components.Node import node
from components.output import OUTPUT


class gate(node):

    def __init__(self, Type, Type_of_gate, size):
        super().__init__(Type)
        self.size = size
        self.Type_of_gate = Type_of_gate
        self.connections = list()

        



    def add_connection(self,connection):
        self.connections.append(connection)


    def calc_output(self):
        list_of_IN_port = list()
        for connection in self.connections:
            if self == connection.destination:
                list_of_IN_port.append(connection.PORT)
        in_port_1 = list_of_IN_port[0]
        in_port_2 = list_of_IN_port[1]
        if (len(in_port_1) == 0 or len(in_port_2) == 0):
            return None
        
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
    

    def pass_output_to_ports(self, output, connection):
        connection.PORT = output
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


    


