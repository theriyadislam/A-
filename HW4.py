# Practical lesson 4. Conditional operators
# Solve the following problems using conditional operators.
#  4.1) When registering on the sites, you must enter your password twice. This is done for security, as this approach reduces the possibility of incorrect password entry. Write a program that compares the password and its confirmation. If they match, the program outputs: "Password accepted", otherwise: "Password not accepted".
# 4.2) Write a program that determines which type of seat in the reserved car (upper or lower, compartment or side) by the specified seat number.
# 4.3) A leap year is considered if its number is a multiple of 4 but not a multiple of 100, or if it is a multiple of 400. Write a function that determines whether the year with the given number is a leap year. If the year is a leap year, then print "Year ... - leap year", where instead of an ellipsis, print the year, otherwise print "This is not a leap year".
# 4.4) Red, blue and yellow are called primary colors because they cannot be obtained by mixing other colors. When mixing the two primary colors, a secondary color is obtained:
# - if you mix red and blue, you get purple;
# - if you mix red and yellow, you get orange.;
# - if you mix blue and yellow, you get green.
# Write a program that reads the names of the two primary colors for mixing. If the user enters anything other than the names "red", "blue" or "yellow", the program should display an error message. Otherwise, the program should print the name of the secondary color that will result.







# 4.1 Password confirmation
# # Read password and confirmation
password = input("Enter password: ")
confirm = input("Confirm password: ")

# Compare using conditional operator
if password == confirm:
    print("Password accepted")
else:
    print("Password not accepted")



# 4.2 Seat type in a reserved car (platzkart)
# Read seat number (assuming integer between 1 and 54)
seat = int(input("Enter seat number (1-54): "))

# Determine type
if 1 <= seat <= 36:
    if seat % 2 == 1:          # odd numbers
        seat_type = "lower compartment"
    else:                       # even numbers
        seat_type = "upper compartment"
elif 37 <= seat <= 54:
    if seat % 2 == 1:
        seat_type = "lower side"
    else:
        seat_type = "upper side"
else:
    seat_type = "invalid seat number"

print(seat_type)

# 4.3 Leap year determination
def check_leap_year(year):
    # Leap year condition: divisible by 4 but not by 100, or divisible by 400
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f"Year {year} - leap year")
    else:
        print("This is not a leap year")

# Example usage
year = int(input("Enter year: "))
check_leap_year(year)


# 4.4 Mixing primary colors
# Read two color names
color1 = input("Enter first primary color (red, blue, yellow): ").strip().lower()
color2 = input("Enter second primary color (red, blue, yellow): ").strip().lower()

# Define set of valid primary colors
primaries = {"red", "blue", "yellow"}

# Validate inputs
if color1 not in primaries or color2 not in primaries:
    print("Error: Please enter only red, blue, or yellow.")
else:
    # Determine the resulting secondary color
    if {color1, color2} == {"red", "blue"}:
        print("purple")
    elif {color1, color2} == {"red", "yellow"}:
        print("orange")
    elif {color1, color2} == {"blue", "yellow"}:
        print("green")
    else:
        # If both colors are the same, the result is the same color (though not a secondary color)
        # The problem statement doesn't specify this case; we can either output the same color or treat as error.
        # Here we'll output the color itself as it remains unchanged.
        print(color1)  # or handle as you wish