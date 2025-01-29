# python 01-script.py 

# double underscore == dunder 

# operator overloading (using magic methods)

class Employee :
    
    def __init__(self, id, name):
        self.id = id 
        self.name = name 

    def __eq__(self, other):
        # return self.id == other.id     
        return self.id == other.id and self.name == other.name
    
    def emp_data(self):
        print(self.id, self.name)
    
emp1 = Employee(101, 'Sonu')
emp2 = Employee(101, 'Sonu')

print(emp1.id, emp1.name)
print(emp2.id, emp2.name)
print(emp1 == emp2)
# print(emp1.__eq__(emp2))
# print(emp1 > emp2) 
# print(emp1 + emp2)







