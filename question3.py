# Multiplication Pattern Analyzer

n = int(input("Enter a number:"))

for i in range(1, 11):
    if i % 2 != 0:
        print(f"{n} x {i} = {n*i} - Odd")
    else:
        print(f"{n} x {i} = {n*i} - Even")
