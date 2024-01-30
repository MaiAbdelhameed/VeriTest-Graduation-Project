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

    def has_any_empty_ports(self):
        dict_of_ports = dict()
        for connection in self.connections:
            if self == connection.destination:
                if len(connection.PORT) == 0:
                    return True, None
                dict_of_ports.update({connection.port_number:connection.PORT})
        return False, dict_of_ports
    def calc_output(self):
        list_of_IN_port = list()
        output = list()
        for connection in self.connections:
            if self == connection.destination:
                list_of_IN_port.append(connection.PORT)
        if self.Type_of_gate == "concat":
            has_empty, dict_of_ports = self.has_any_empty_ports()
            if not has_empty:
                for i in range(len(list_of_IN_port)):
                    output.append(dict_of_ports[i])
                
        else:
  
            in_port_1 = list_of_IN_port[0]
            in_port_2 = list_of_IN_port[1]
            if (len(in_port_1) == 0 or len(in_port_2) == 0):
                return None
            
            
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
    

    def pass_output_to_ports(self, output, connections):
        for connection in connections:
            connection.PORT = output
            if isinstance(connection.destination, OUTPUT):
                list_of_connections = list()
                list_of_connections.append(connection)
                connection.destination.process_node(list_of_connections)
        



    def process_node(self, connections):
        output = self.calc_output()
        if output == None:
            return False
        self.pass_output_to_ports(output, connections)
        return True




    
    def __str__(self):
        return super().__str__()


    


