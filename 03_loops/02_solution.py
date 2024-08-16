# Problem: Calculate the sum of even numbers up to a given number n.

num = int(input("Enter the number: "))
sum_num = 0

for i in range(1, num + 1):
    if i % 2 == 0:
        sum_num += i

print("Sum of even numbers is", sum_num)