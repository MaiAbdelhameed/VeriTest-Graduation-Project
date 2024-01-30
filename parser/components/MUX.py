from components.Node import node

class mux(node):

    def __init__(self, Type):
        super().__init__(Type)
        self.connections = list()


    def add_connection(self, connection):
        self.connections.append(connection)
        self.list_of_IN_port = list()
   
    def calc_output(self):
        true_value = list()
        false_value = list()
        selector_value = str()
        for connection in self.connections:
            if self == connection.destination:
                if connection.isTrueValue:
                    true_value = connection.PORT
                elif connection.isFalseValue:
                    false_value = connection.PORT
                else:
                    selector_value = connection.PORT

        if selector_value == "0":
            return true_value
        return false_value
        

    def pass_output_to_ports(self, output):
        for connection in self.connections:
            if self == connection.source:
                connection.PORT = output
            else:
                pass
        
        
    def process_node(self, connection):
        if self == connection.source:
            if len(self.list_of_IN_port) != 3:
                return False
            output = self.calc_output()
            self.pass_output_to_ports(output)
            connection.destination.process_node(connection)
            return True
        else:
            self.list_of_IN_port.append([])



        

