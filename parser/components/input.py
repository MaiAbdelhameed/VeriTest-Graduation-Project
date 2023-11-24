class Input():

    def __init__(self, Type, size, start, end, name):
        #super().__init__(Type)
        self.start = start
        self.end = end
        self.name = name
        self.size = size

    
    def connect_input(self, input):
        self.input1 = input


    def calculate_output(self):
        self.output = reversed(self.input1)
        return True
        
    

    # def __str__(self):
    #     return super().__str__()


    


