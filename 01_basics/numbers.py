# Calculate (x + y) * z
x = 2  # integer
y = 3  # integer
z = 4  # integer

result = (x + y) * z
print(result)
print((x + y) * z)
print(40 + 5.5)
print(x + 1, y * 2)

# Addition of integer and float
print(40 + 5.5)  # float

# Print x + 1 and y * 2 as separate values
print(x + 1, y * 2)  # 3 6
print(oct(10))
print(bin(64))
print(hex(10))

# Convert integer to octal, binary, and hexadecimal
print(oct(10))  # '0o12'
print(bin(64))  # '0b1000000'
print(hex(10))  # '0xa'
print(int("64", 8))
print(int("1000", 2))
print(int("64", 16))

# Convert string to integer in octal, binary, and hexadecimal
print(int("64", 8))  # 56
print(int("1000", 2))  # 8
print(int("64", 16))  # 100

# Import math module and use trunc function
import math

# Truncate a float to the nearest integer
print(math.trunc(5.5))  # 5