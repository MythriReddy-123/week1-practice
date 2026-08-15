# Remove Repeated Consecutive Values

values = [10, 10, 20, 20, 20, 30, 10, 10, 40]

new = []

for val in values:
    if not new or new[-1] != val:
        new.append(val)

print(f"Original List: {values}")
print(f"Result: {new}")
