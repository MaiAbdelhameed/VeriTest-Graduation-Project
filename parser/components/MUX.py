from components.Node import node
from components.output import OUTPUT


class mux(node):

    def __init__(self, Type):
        super().__init__(Type)
        self.connections = list()


    def add_connection(self, connection):
        self.connections.append(connection)
        
   
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

        
        if len(true_value) == 0 or len(false_value) == 0 or len(selector_value) == 0:
            return None

        if selector_value == "0":
            return true_value
        return false_value
        

    def pass_output_to_ports(self, output, connection):
        connection.PORT = output
        if isinstance(connection.destination, OUTPUT):
            connection.destination.process_node(connection)
        
        
    def process_node(self, connection):
        output = self.calc_output()
        if output == None:
            return False
        self.pass_output_to_ports(output, connection)
        connection.destination.process_node(connection)
        return True
        



        

