# 8.1 Create a dictionary of countries and their capitals
countries_capitals = {
    "Ukraine": "Kyiv",
    "France": "Paris",
    "Germany": "Berlin",
    "Italy": "Rome",
    "Spain": "Madrid",
    "Japan": "Tokyo",
    "USA": "Washington, D.C.",
    "UK": "London"
}

# a) Display all key-value pairs
print("a) All countries and their capitals:")
for country, capital in countries_capitals.items():
    print(f"{country} -> {capital}")

# b) Display the capital for a certain country (example: Germany)
certain_country = "Germany"
print(f"\nb) Capital of {certain_country}: {countries_capitals.get(certain_country, 'Not found')}")

# c) Sort and display the dictionary in alphabetical order of country names
print("\nc) Sorted by country name:")
for country in sorted(countries_capitals.keys()):
    print(f"{country} -> {countries_capitals[country]}")





# ________________________________________________________________________________________________





def build_scrabble_scores():
    """Parse the problem's scoring rules into a dictionary."""
    score_data = [
        ("A, B, E, I, N, O, R, S, T", 1),
        ("D, K, L, M, P, Y", 2),
        ("B, D, E, B, I", 3),
        ("Y, Y", 4),
        ("W, W, X, C, H", 5),
        ("W, E, Y", 8),
        ("F, Sch, B", 10)
    ]
    scores = {}
    for letters_str, points in score_data:
        # Split by comma, strip spaces, and handle each item
        for item in letters_str.split(','):
            item = item.strip()
            if len(item) == 1:
                scores[item.upper()] = points
            else:
                # Expand multi-character item into single letters (e.g., "Sch" -> S, c, h)
                for ch in item:
                    scores[ch.upper()] = points
    return scores

def word_score(word, scores):
    """Return the total Scrabble score for the given word."""
    total = 0
    for ch in word.upper():
        total += scores.get(ch, 0)
    return total

# Build the scoring dictionary
scrabble_scores = build_scrabble_scores()

# User input
user_word = input("Enter a word: ").strip()
if user_word:
    print(f"Score for '{user_word}': {word_score(user_word, scrabble_scores)}")
else:
    print("No word entered.")




# ________________________________________________________________________________________________




# Sample data: student -> set of languages they know
students_languages = {
    "Alice": {"English", "French", "Chinese"},
    "Bob": {"Spanish", "German"},
    "Carol": {"Chinese", "Japanese", "English"},
    "David": {"Russian", "Arabic"},
    "Eve": {"Chinese", "Korean"}
}

# a) Determine all different languages (union of all sets)
all_languages = set()
for langs in students_languages.values():
    all_languages.update(langs)

# Print sorted list of languages
print("All languages (sorted):")
for lang in sorted(all_languages):
    print(lang)

# b) List students who know Chinese
chinese_students = [name for name, langs in students_languages.items() if "Chinese" in langs]
print("\nStudents who know Chinese:")
for student in sorted(chinese_students):
    print(student)



# ________________________________________________________________________________________________




