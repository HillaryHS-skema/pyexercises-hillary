"""Exercise 8.0 — Operators (bonus, not graded)

WHAT THE PROGRAM MUST DO
    Take two values of your choice and display, as a readable table, the result of every
    comparison between them and of the logical combinations of those results.

ANSWER THESE FIRST, in comments
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which two values did you pick, and which comparison result surprised you?

WHAT THE AI CANNOT KNOW
    Your two values. Pick a pair where the answer is not obvious: two strings with
    different capitalisation, a number and the same number written as text, or zero and
    an empty string.

CHECK IT YOURSELF
    Predict each result before running. Count how many you got right.

DELIVERABLE
    This file, with your comments and your code.
"""


# 1. What goes in?
# Two values: "Paris" and "paris".

# 2. What happens to it?
# The program compares the two values using comparison operators:
# ==, !=, >, <, >=, <=
# It also uses logical operators: and, or, not.
# The results are displayed in readable tables.

# 3. What comes out?
# Tables showing the comparison results and logical combinations.
# All results are displayed as True or False.

# 4. Which two values did I pick, and what surprised me?
# I chose "Paris" and "paris".
# I was surprised that "Paris" < "paris" is True.
# Python compares strings based on character values,
# and uppercase letters come before lowercase letters.


# Your code below

# Step 1: Choose two values
a = "Paris"
b = "paris"

print("EXERCISE 8.0 — OPERATORS")
print("First value:", a)
print("Second value:", b)


# Step 2: Comparison operators
print("\nCOMPARISON OPERATORS")
print("-" * 40)
print(f"{'Comparison':<20} {'Result':<10}")
print("-" * 40)

comparisons = {
    "a == b": a == b,
    "a != b": a != b,
    "a > b": a > b,
    "a < b": a < b,
    "a >= b": a >= b,
    "a <= b": a <= b
}

for comparison, result in comparisons.items():
    print(f"{comparison:<20} {str(result):<10}")


# Step 3: Logical operators
print("\nLOGICAL OPERATORS")
print("-" * 50)
print(f"{'Expression':<35} {'Result':<10}")
print("-" * 50)

equal = a == b
greater = a > b
smaller = a < b

logical_results = {
    "equal and greater": equal and greater,
    "equal or greater": equal or greater,
    "greater and smaller": greater and smaller,
    "greater or smaller": greater or smaller,
    "not equal": not equal,
    "not greater": not greater,
    "not smaller": not smaller
}

for expression, result in logical_results.items():
    print(f"{expression:<35} {str(result):<10}")


# Step 4: All combinations of comparison results
print("\nALL PAIRWISE LOGICAL COMBINATIONS")
print("-" * 65)
print(f"{'Expression':<50} {'Result':<10}")
print("-" * 65)

for name1, result1 in comparisons.items():
    for name2, result2 in comparisons.items():
        print(f"{name1} and {name2}: {result1 and result2}")
        print(f"{name1} or {name2}: {result1 or result2}")


# Step 5: Show final message
print("\nExercise completed!")
print("All comparison and logical results have been displayed.")
