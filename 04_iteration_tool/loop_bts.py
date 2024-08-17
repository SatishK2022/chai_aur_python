# Open the script.py file
f = open('./script.py')

# Print the first 4 lines of the file
print(f.readline())  # Print the first line of the file
print(f.readline())  # Print the second line of the file
print(f.readline())  # Print the third line of the file
print(f.readline())  # Print the fourth line of the file

# Print the next line of the file
print(f.__next__())  # Print the next line of the file

# Read and print all the lines of the file
for line in open('./script.py'):
    print(line)

# Read and print all the lines of the file until there are no more lines
while True:
    line = f.readline()  # Read the next line of the file
    if not line: break  # If there are no more lines, break the loop
    print(line, end='')  # Print the line without a newline character

# Check if the string is empty
test = "Satish"
if not test:  # If the string is empty, print a message
    print("String is empty")

# Check if the string is empty
test = ""
if not test:  # If the string is empty, print a message
    print("String is empty")

# Create an iterator object from the list
myList = [1, 2, 3, 4, 5]

I = iter(myList)
print(I)

# Use the iterator object to print the elements of the list
print(I.__next__())
print(I.__next__())
print(I.__next__())
print(I.__next__())

# The iterator object is exhausted, calling __next__() again will raise a StopIteration exception
try:
    print(I.__next__())
except StopIteration:
    print("The iterator object is exhausted")
print(I.__next__())



print(iter(f) is f)


myDict = {'a': 'One', 'b': 'Two'}

# for key in myDict.keys():
#     print(key)

