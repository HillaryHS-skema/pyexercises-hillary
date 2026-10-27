"""Exercise 2.1 — Transforming text (homework)

WHAT THE PROGRAM MUST DO
    Ask the user for a sentence, then display four different transformations of it.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which four transformations did you choose, and in what situation would each of
       them be useful? One line each.

WHAT THE AI CANNOT KNOW
    Your four transformations. Pick them yourself. Open ../examples/strings/string_methods.py
    to see what is available, then choose, then justify.

    A transformation that produces the same thing as another one does not count as two.

CHECK IT YOURSELF
    Run it with a sentence that has spaces at both ends and a capital in the middle.
    For each of your four results, say in a comment whether it is what you expected.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: A sentence entered by the user about fashion.
# 2. Process: The program applies four different text transformations to the sentence.
# 3. Out: The sentence without extra spaces, in uppercase, in lowercase, and in title case.
# 4. My four transformations, and when each is useful:
# strip(): Removes extra spaces from customer input.
# upper(): Creates uppercase text for fashion promotions.
# lower(): Standardizes text for easy comparison.
# title(): Formats fashion product names and titles.


# Your code below
sentence = input("Enter a sentence about fashion: ")

# Remove extra spaces at the beginning and end
print("Without extra spaces:", sentence.strip())

# Convert to uppercase
print("Uppercase:", sentence.upper())

# Convert to lowercase
print("Lowercase:", sentence.lower())

# Capitalize the first letter of each word
print("Title case:", sentence.title())
