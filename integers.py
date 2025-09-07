# Integers are whole numbers without any fractional or decimal part. They can be positive, negative, or zero.
a = 10  # positive integer
b = -5  # negative integer
c = 0   # zero

# Basic Arithmetic Operations
x = 10
y = 5
print(x + y)   # Addition --> 15
print(x - y)   # Subtraction --> 5
print(x * y)   # Multiplication --> 50
print(x / y)   # Division --> 2.0(float result)

# Modulus (remainder of division):
print(x % y)   # Modulus --> 0

# Integer Division & Floor Division
print(x // y)   # Floor division --> 2

# Design a simple calculator that performs operations on two integers provided by the user.

num1 = int(input("Enter First number:"))
num2 = int(input("Enter Second number:"))

add = num1 + num2
sub = num1 - num2
mul = num1 * num2
div = num1 / num2
div_floor = num1 // num2

print(add)
print(sub)
print(mul)
print(div)
print(div_floor)
