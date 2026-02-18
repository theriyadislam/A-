# Practical Exercise 3. Linear algorithms. Operator precedence.

# 3.1 Calculating the area of a circle
print("3.1 Area of a circle")
r = float(input("Enter the radius of the circle: "))
pi = 3.14159
s = pi * r ** 2
print(f"Area of a circle with radius {r} is {s:.5f}\n")

# 3.2 Solving a linear equation ax + b = 0
print("3.2 Solving a linear equation ax + b = 0")
a = float(input("Enter a: "))
b = float(input("Enter b: "))
if a == 0:
    if b == 0:
        print("The equation has infinitely many solutions (x can be any number)\n")
    else:
        print("The equation has no solutions\n")
else:
    x = -b / a
    print(f"Solution: x = {x}\n")

# 3.3 Temperature conversion from Celsius to Fahrenheit
print("3.3 Temperature conversion")
c = float(input("Enter temperature in degrees Celsius: "))
f = (9/5) * c + 32
print(f"{c} °C = {f} °F\n")

# 3.4 Calculating the arithmetic mean of three numbers
print("3.4 Arithmetic mean of three numbers")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))
average = (num1 + num2 + num3) / 3
print(f"The arithmetic mean of {num1}, {num2}, {num3} is {average}\n")

# 3.5 Checking operator precedence
print("3.5 Checking operator precedence")
expr1 = 5 + 2 * 3 - 4 / 2
print(f"5 + 2 * 3 - 4 / 2 = {expr1}")

expr2 = (3 + 5) * (2 + 4) / 2
print(f"(3 + 5) * (2 + 4) / 2 = {expr2}")

expr3 = -3 + 6 / 2 * 4
print(f"-3 + 6 / 2 * 4 = {expr3}")

expr4 = 5 + 4 * 5 ** 2 + 7
print(f"5 + 4 * 5 ** 2 + 7 = {expr4}")

