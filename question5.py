# Bus Seat Availability Manager

seats = [
    "Available",
    "Booked",
    "Available",
    "Available",
    "Booked",
    "Available",
    "Booked",
    "Available"
]

for i in range(len(seats)):
    print(f"Seat {i+1}: {seats[i]}")

seat_num = int(input("Enter a seat number: "))
if seats[seat_num-1] == "Available":
    seats[seat_num-1] = "Booked"
    print("Seat booked successfully.")
else:
    print("Seat is already booked.")

booked = 0
available = 0
for seat in seats:
    if seat == "Booked":
        booked += 1
    else:
        available += 1


print(f"Total Seats: {len(seats)}")
print(f"Booked Seats: {booked}")
print(f"Available Seats: {available}")