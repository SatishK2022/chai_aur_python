# Problem: Write a function that takes variable number of arguments and returns their sum.

def sum_all(*args):
    print(args)  # It returns a tuple (1, 2, 3, 4)
    # Iterate over the arguments and print each element
    for i in args:
        print(i * 2)

    # Return the sum of all the arguments
    return sum(args)

# Call the function and print the result
print(sum_all(1, 2, 3, 4))
# print(sum_all(1, 2, 3, 4, 5, 6, 7, 8))
# print(sum_all(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))