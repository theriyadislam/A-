# 3.1 Calculating the area of a circle
print("3.1 Area of a circle")
r = float(input("Enter radius r: "))
pi_approx = 3.14159
area = pi_approx * r ** 2
print(f"Area = {area:.4f}\n")

# 3.2 Solution of the linear equation
print("3.2 Linear equation ax + b = 0")
a = float(input("Enter a: "))
b = float(input("Enter b: "))
if a == 0:
    if b == 0:
        print("Infinite solutions (any x works)")
    else:
        print("No solution")
else:
    x = -b / a
    print(f"x = {x:.4f}\n")

# 3.3 Temperature conversion
print("3.3 Celsius to Fahrenheit")
c = float(input("Enter temperature in Celsius: "))
f = (9/5) * c + 32
print(f"{c}°C = {f:.2f}°F\n")

# 3.4 Calculation of the arithmetic mean
print("3.4 Arithmetic mean of three numbers")
nums = []
for i in range(1, 4):
    num = float(input(f"Enter number {i}: "))
    nums.append(num)
mean = sum(nums) / len(nums)
print(f"Arithmetic mean = {mean:.4f}\n")

# 3.5 Priority check – evaluate given expressions
print("3.5 Expression evaluation (operator precedence)")
expr1 = 5 + 2 * 3 - 4 / 2
expr2 = (3 + 5) * (2 + 4) / 2
expr3 = -3 + 6 / 2 * 4
expr4 = 5 + 4 * 5 ** 2 + 7

print("5 + 2 * 3 - 4 / 2 =", expr1)
print("(3 + 5) * (2 + 4) / 2 =", expr2)
print("-3 + 6 / 2 * 4 =", expr3)
print("5 + 4 * 5 ** 2 + 7 =", expr4)