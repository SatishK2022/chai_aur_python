# Problem: Compute the factorial of a number using a while loop.

number = int(input("Enter a number:"))

fact = 1

while number > 0:
    fact *= number
    number -= 1

print("Factorial is", fact)