# Parking Fee Calculator

def parking_fee(hours):
    if hours <= 2:
        return 30 * hours
    elif 3 <= hours <= 5:
        return 25 * hours
    elif hours > 5:
        return 20 * hours


hours = int(input("Enter parking hours: "))
result = parking_fee(hours)
print(f"Parking Charge: ₹{result}")

if result >= 150:
    print("Service Charge: ₹20")
    print(f"Final Amount: ₹{result + 20}")
else:
    print("Service Charge: ₹0")
    print(f"Final Amount: ₹{result}")