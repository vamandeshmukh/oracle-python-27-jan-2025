
# OOP 
# class object 

# entity - attributes, functinalities 
# employee - id, name, salary, ... work(), write_code(), leave(), ... 


# employee = {'id': 101, 'name': 'Sonu'}

# class 
# fields, functions 

# class Employee :
#     pass
# emp1 = Employee()

# # simple class example 
# class Employee :
    
#     def emp_data(self):
#         print('employee class')
    

# emp1 = Employee()
# emp1.emp_data()


# simple class example 
class Employee :
    
    # special method == constructor 
    def __init__(self, id, name):
        self.id = id 
        self.name = name 
    
    def emp_data(self):
        print(self.id, self.name)
    
# emp1 = Employee() # call to constructor - __init__(self):

emp1 = Employee(101, 'Sonu')
emp1.emp_data()





