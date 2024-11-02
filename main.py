class IOString:
    def __init__(self):
        self.str1 = ""

    def get_String(self):
        self.str1 = input("Enter String: ")

    def display(self):
        print("String is",self.str1.upper()) 


io_string = IOString()
io_string.get_String()  
io_string.display()  

        
