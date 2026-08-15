# Employee Record Analyzer

employee = ("Arjun", "Developer", 45000, 3)

emp_name, role, salary, exp = employee

if exp < 2:
    bonus_str = "5%"
    bonus_pct = 0.05
elif 2 <= exp < 5:
    bonus_str = "10%"
    bonus_pct = 0.10
else:
    bonus_str = "15%"
    bonus_pct = 0.15

monthly_bonus = salary * bonus_pct
annual_salary = salary * 12
total_annual_comp = annual_salary + (monthly_bonus * 12)

print(f"Employee Name: {emp_name}")
print(f"Designation: {role}")
print(f"Experience: {exp}")
print(f"Monthly Salary: {salary}")
print(f"Annual Salary: {annual_salary}")
print(f"Bonus: {bonus_str}")
print(f"Total Salary Compensation: {total_annual_comp}")



