username = "satish"  # Global variable


def func():
    print(username)  # Accessing the global variable


print(username)
func()

x = 99
# def func2(y):
#     z = x + y
#     return z

# print(func2(1))


# def func3():
#     global x  # Avoiding the use of global variable
#     x = 88

# func3()
# print(x)


def f1():
    x = 20
    def f2():
        print(x)
    return f2


myResult = f1()
myResult()


def chaicoder(num):
    def actual(x):
        return x ** num
    return actual


f = chaicoder(2)
g = chaicoder(3)

print(f(3))
print(g(3))