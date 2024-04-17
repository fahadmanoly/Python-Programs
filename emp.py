employees = [
    {"name": "Alice", "department": "Sales", "salary": 50000},
    {"name": "Bob", "department": "IT", "salary": 60000},
    {"name": "Charlie", "department": "Sales", "salary": 55000},
    {"name": "Dave", "department": "IT", "salary": 70000},
    {"name": "Eve", "department": "Marketing", "salary": 45000}
]

def avg_salary_by_department(employees, department):
    department_employees = [e for e in employees if e["department"] == department]
    if len(department_employees) == 0:
        return None
    total_salary = sum(e["salary"] for e in department_employees)
    return total_salary / len(department_employees)

department = "Marketing"
avg_salary = avg_salary_by_department(employees, department)
if avg_salary is None:
    print(f"No employees found in the {department} department")
else:
    print(f"The average salary of employees in the {department} department is {avg_salary:.2f}")
    