#include <iostream>
#include <string>

using namespace std;

class Employee {

public:

    string name;
    double salary;

    void empInfo() {
        cout << "My name is " << name << " and my salary is ₹" << salary << "." << endl;
    }
};

int main() {
    Employee emp;

    emp.name = "Sonu Reddy";
    emp.salary = 12.25;

    emp.empInfo();

    return 0;
}
