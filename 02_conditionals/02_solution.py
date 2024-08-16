# Problem: Movie tickets are priced based on age: $12 for adults (18 and over), $8 for children. Everyone gets a $2 discount on Wednesday.

age = int(input("Enter your age: "))
day = str(input("Enter the day: ").lower())

price = 0

# if age >= 18:
#     price = 12
# else:
#     price = 8

# print(price)

price = 12 if age >= 18 else 8 # Shorthand property of above code

if day == "wednesday":
    price -= 2

print("Ticket price for you is $",price)