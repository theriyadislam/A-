
# 5.1: Combine N words with spaces
n = int(input("Enter the number of words: "))
words = []
for i in range(n):
    word = input(f"Enter word {i+1}: ")
    words.append(word)
result = " ".join(words)
print("Combined string:", result)



# 5.2: Combine words until "stop" is entered
words = []
while True:
    word = input("Enter a word (or 'stop' to finish): ")
    if word.lower() == "stop":
        break
    words.append(word)
result = " ".join(words)
print("Combined string:", result)



# 5.3: Check if words contain the letter 'f' (rare)
print("Enter words to check (press Enter alone to quit):")
while True:
    word = input("Word: ")
    if word == "":
        break
    if 'f' in word.lower():
        print("Wow! It's a rare word!")
    else:
        print("Oh, it's not a very rare word...")



# 5.4: Math game – sums until 3 mistakes
import random

mistakes = 0
correct = 0

print("Welcome to the Math Game!")
print("Solve the sums. You have 3 mistakes allowed.\n")

while mistakes < 3:
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    correct_sum = a + b
    
    # Print the expression and keep cursor on the same line
    user_input = input(f"{a} + {b} = ")
    
    try:
        answer = int(user_input)
    except ValueError:
        print("Please enter a valid integer.")
        continue
    
    if answer == correct_sum:
        print("Correct!")
        correct += 1
    else:
        print("The answer is incorrect")
        mistakes += 1

print(f"\nThe game is over. Correct answers: {correct}")