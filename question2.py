# Movie Ticket Booking Summary

def ticket_booking(name, age, ticket):
    if age < 12:
        ticket_price = 120
    elif 12 <= age <= 59:
        ticket_price = 200
    else:
        ticket_price = 150
    
    total = ticket_price * tickets
    return ticket_price, total


customer_name = input("Enter your name: ")
age = int(input("Enter your age: "))
tickets = int(input("Enter no. of tickets: "))


ticket_price, total = ticket_booking(customer_name, age, tickets)

if tickets >= 5:
    discount = 0.10 * total
else:
    discount = 0

final_amount = total - discount

print("=" * 50)
print(f"Customer Name: {customer_name}")
print(f"Ticket Price: ₹{ticket_price}")
print(f"Number of Tickets: {tickets}")
print(f"Total Before Discount: ₹{total}")
print(f"Discount: ₹{discount}")
print(f"Final Amount: ₹{final_amount}")
print("=" * 50)
