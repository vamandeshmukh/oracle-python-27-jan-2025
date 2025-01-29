# import employee 
import employee as em 
from employee import Employee, Department

def get_emp():
    # import employee as em 
    emp = em.Employee(101, 'Sonu')
    # from employee import Employee
    emp = Employee(102, 'Monu')
    dep = em.Department()
    # dep = Department()
    
    emp.emp_data() 
    
