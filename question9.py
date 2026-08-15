# Message Slicing Tool

s = input("Enter a message: ")

print(f"First 5 characters: {s[:5]}")
print(f"Last 5 characters: {s[-5:]}")
print(f"Characters from Index 2 to 7: {s[2:8]}")
print(f"Every Second Character: {s[::2]}")
print(f"Message in Reverse: {s[::-1]}")
print(f"Message without First and Last Character: {s[1:-1]}")