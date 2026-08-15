# Expense Tracker

expenses = [250, 1200, 450, 800, 150, 2000, 350]

print("Total Expense: ", sum(expenses))
print("Average Expense: ", sum(expenses)/len(expenses))
print("Highest Expense: ", max(expenses))
print("Lowest Expense: ", min(expenses))

above = 0
below = 0
for i in range(len(expenses)):
    if expenses[i] > 500:
        above += 1
    else:
        below += 1

print("Number of Expenses Above 500: ", above)
print("Number of Expenses Below or Equal to 500: ", below)

print("Expenses Above Average: ")
for i in expenses:
    if i > (sum(expenses)/len(expenses)):
        print(i)