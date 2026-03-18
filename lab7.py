# 7.1) Check if a user's number exists in a predefined list
# Create a list of five numbers
numbers = [3, 7, 15, 22, 8]

# Ask the user for a number
try:
    user_num = int(input("Enter a number: "))
except ValueError:
    print("Invalid input. Please enter an integer.")
    exit()

# Check if the number is in the list
found = user_num in numbers
 
# Print results
print(f"Source list: {numbers}")
print(f"Your number: {user_num}")
if found:
    print("Congratulations, you guessed the number!")
else:
    print("There is no such number!")




# 7.2) Find duplicate items in a list
# Create any list (example with duplicates)
my_list = [5, 2, 8, 5, 1, 9, 2, 3, 5]

# Find duplicates using a set to track seen items
seen = set()
duplicates = set()

for item in my_list:
    if item in seen:
        duplicates.add(item)
    else:
        seen.add(item)

# Output duplicates
if duplicates:
    print(f"Duplicate values found: {', '.join(map(str, duplicates))}")
else:
    print("No duplicates found.")






# 7.3) Days of week: days off and working days
# Tuple with days of the week
days_of_week = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")

# Ask user for number of days off (0–7)
try:
    days_off_count = int(input("How many days off per week do you want? "))
    if days_off_count < 0 or days_off_count > 7:
        raise ValueError("Number must be between 0 and 7.")
except ValueError as e:
    print(f"Invalid input: {e}")
    exit()

# Select days off from the end of the tuple
days_off = list(days_of_week[-days_off_count:]) if days_off_count > 0 else []

# Working days are the remaining ones
working_days = list(days_of_week[:-days_off_count]) if days_off_count > 0 else list(days_of_week)

# Display results
print(f"Your days off: {days_off}")
print(f"Your working days: {working_days}")






# 7.4) Two groups of students and a sports team
import random

# Two lists of 10 surnames each
group_a = [
    "Smith", "Johnson", "Williams", "Jones", "Brown",
    "Davis", "Miller", "Wilson", "Moore", "Taylor"
]

group_b = [
    "Anderson", "Thomas", "Jackson", "White", "Harris",
    "Martin", "Thompson", "Garcia", "Martinez", "Robinson"
]

# a) Create a sports team (tuple) of any 5 students from each group
# Option 1: take first 5 (deterministic)
# team = tuple(group_a[:5] + group_b[:5])

# Option 2: randomly select 5 (more realistic)
team = tuple(random.sample(group_a, 5) + random.sample(group_b, 5))

# b) Display original lists and the new tuple
print("Group A:", group_a)
print("Group B:", group_b)
print("Sports team:", team)

# c) Output its length
print(f"Team size: {len(team)}")

# d) Sort the tuple alphabetically (returns a list, we can convert to tuple)
sorted_team = tuple(sorted(team))
print("Sorted team (alphabetically):", sorted_team)

# e) Determine if "Ivanov" is in the team and count occurrences
name = "Ivanov"
count = team.count(name)
if count > 0:
    print(f"The surname '{name}' appears in the team {count} time(s).")
else:
    print(f"The surname '{name}' is not in the team.")