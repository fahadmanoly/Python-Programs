employees = [
    {"name": "Alice", "department": "Sales", "salary": 50000},
    {"name": "Bob", "department": "Sales", "salary": 60000},
    {"name": "Charlie", "department": "Engineering", "salary": 70000},
    {"name": "David", "department": "Engineering", "salary": 80000},
    {"name": "Eve", "department": "Sales", "salary": 55000},
    {"name": "Frank", "department": "Engineering", "salary": 75000}
]

department_totals = {}

# Step 1: Calculate total salary and employee count for each department
for employee in employees:
    department = employee["department"]
    salary = employee["salary"]
    if department not in department_totals:
        department_totals[department] = {"total_salary": 0, "employee_count": 0}
    department_totals[department]["total_salary"] += salary
    department_totals[department]["employee_count"] += 1

# Step 2: Calculate average salary for each department
for department, totals in department_totals.items():
    average_salary = totals["total_salary"] / totals["employee_count"]
    print(f"Average salary for {department}: {average_salary}")

