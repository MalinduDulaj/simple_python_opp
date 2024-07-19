class Employee:
    # Static variable to keep track of the total number of employees
    total_employees = 0

    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

        # Increment the total number of employees when a new employee is created
        Employee.total_employees += 1

    # Instance method to display employee information
    def display_info(self):
        print(f"Employee ID: {self.emp_id}")
        print(f"Name: {self.name}")
        print(f"Salary: {self.salary}")

# Creating employee objects
emp1 = Employee(101, "Saman", 50000)
emp2 = Employee(102, "Kamal", 60000)
emp3 = Employee(102, "Nimal", 60000)

# Displaying employee information
print("Employee 1 Information:")
emp1.display_info()
print()

print("Employee 2 Information:")
emp2.display_info()
print()

# Accessing the static variable using the class name
print("Total Employees:", Employee.total_employees)

      
