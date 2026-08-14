# Character Category Counter


def char_count(text):
    upper_case = 0
    lower_case = 0
    digits = 0
    spaces = 0
    other = 0
    for c in text:
        if c.isupper():
            upper_case += 1
        elif c.islower():
            lower_case += 1
        elif c.isdigit():
            digits += 1
        elif c == " ":
            spaces += 1
        else:
            other += 1
    
    return upper_case, lower_case, digits, spaces, other


text = input("Enter text: ")
upper_case, lower_case, digits, spaces, other = char_count(text)

print("Uppercase letters:", upper_case)
print("Lowercase letters:", lower_case)
print("Digits:", digits)
print("Spaces:", spaces)
print("Other characters:", other)
