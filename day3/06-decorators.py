# # Decorators in Python 

# # custom decorator 
# def data_accessed(func):
#     def wrapper(*args):
#             print('emp data accessed.')
#             return func(*args)
#     return wrapper

# # decorator used in this class 
# class Employee :
    
#     def __init__(self, id, name):
#         self.id = id 
#         self.name = name 

#     # @property #built-in decorator in Python 
#     # def get_name(self):
#     #     return self.name
    
#     @data_accessed
#     def emp_data(self):
#         print(self.id, self.name)
    
# emp1 = Employee(101, 'Sonu')
# emp1.emp_data()
# # print(emp1.get_name)


# Decorators in Python 

def data_accessed(func):
    def wrapper(*args):
            print('emp data accessed.')
            print(args)
            return func(*args)
    return wrapper

class Employee :
    
    def __init__(self, id, name):
        self.id = id 
        self.name = name 

    @data_accessed
    def emp_data(self):
        print(self.id, self.name)
    
emp1 = Employee(101, 'Sonu')
emp1.emp_data()

