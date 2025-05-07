print("Hello World!!")

num1 = 10
num2 = 20
result = num1 + num2

print("Sum is:", result)

for i in range(5):
    if i ==3:
        continue
    print(i)

import calendar as c
print(c.month_name[1])

x = lambda a, b, c: a + b + c
print(x(5, 6, 2))


def countdown(num):
    print("Starting")
    while num > 0:
        yield num
        num -= 1
val = countdown(5)
print(next(val))  # Outputs: Starting \n 5

i = j = k = 20

print(i)  # prints 20
print(j)  # prints 20
print(k)  # prints 20

x, y, z = 10, 20, 30

print("x:", x)
print("y:", y)
print("z:", z)

y = 20

def my_function():
    global y
    print("Inside the function, y =", y)
    y = 30  # changing the neighborhood!

my_function()
print("Outside the function, y =", y)

fruits = ["apple", "banana", "cherry"]
print("Second fruit:", fruits[1])
fruits.append("orange")
print("Updated list of fruits:", fruits)
print("*******", type(fruits))