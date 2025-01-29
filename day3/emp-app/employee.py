class Employee :
    
    def __init__(self, id, name):
        self.id = id 
        self.name = name 

    def __eq__(self, other):
        # return self.id == other.id     
        return self.id == other.id and self.name == other.name
    
    def emp_data(self):
        print(self.id, self.name)

class Department:
    pass 