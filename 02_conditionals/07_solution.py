# Problem: Customize a coffee order: "Small", "Medium", or "Large" with an option for "Extra shot" of espresso.

order_size = input("Enter your order size(Small, Medium, Large): ").lower()
extra_shot = input("Do you want extra shot(yes/no)? ").lower()

if extra_shot == "yes":
    coffee = order_size + " coffee with an extra shot"
else:
    coffee = order_size + " coffee"

print(coffee)