
# # # exception and error handling 
# # print(10 / 0)

# print('start')
# nums = [25, 31, 22, 9, 17]

# try: 
#     print(nums[5])
# except IndexError as e:
#     print(f'{e}')
# finally:
#     print('end')


# custom exception creation and handling 

# custom exception class 
class InvalidAgeError (Exception):
    
    def __init__ (self, age, message = 'An exception occured.'):
        self.age =age
        self.message = message
        super().__init__(self.message)
        
# class in which custom exception is raised 
class Employee :
    
    def __init__(self, id, name, age):
        self.id = id 
        self.name = name 
        if age < 18 or age > 65:
            raise InvalidAgeError(age, 'age is invalid')
        self.age = age 
            
    def emp_data(self):
        print(self.id, self.name, self.age)

# custom exception handled 
try:     
    emp1 = Employee(101, 'Sonu', 25)
    emp1.emp_data()
except InvalidAgeError as e:
    print(e)
    
try:
    emp2 = Employee(102, 'Monu', 16)
    emp2.emp_data()
except InvalidAgeError as e:
    print(e)
finally:
    pass
