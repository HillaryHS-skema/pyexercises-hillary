"""Exercise 7.1 — Loading a file, cleaning it, saving the result (homework)

This is the direct rehearsal for the final exam. Session 8 starts with it.

WHAT THE PROGRAM MUST DO
    Load names.txt, clean what is inside, sort it by last name, and write the result to
    a new file. The original file must not be modified.

DO THIS BEFORE ANYTHING ELSE
    Open names.txt and read it with your eyes. Then write, in comments at the top of
    your file, everything that is wrong with it. There are at least four different
    problems. Find them yourself.

    This step is not optional and it is graded. An assistant cannot see your file.

ANSWER THESE, in comments, after the list of problems
    1. What goes in?
    2. What happens to it?  (one line per problem you found, and how you deal with it)
    3. What comes out?
    4. What does "sort by last name" mean when a line contains two words, and how do you
       know which one is the last name?

WHAT THE AI CANNOT KNOW
    The actual content of names.txt. If you paste this brief into an assistant without
    describing the file, it will write a program for a clean file, and that program will
    crash or produce nonsense on the real one.

    Describe the file to it. That description is the exercise.

CHECK IT YOURSELF
    Count the lines in names.txt, then in your output file. The numbers should differ,
    and you should be able to say exactly why. Then check the first and last name of
    your sorted list by hand.

DELIVERABLE
    This file, plus the output file your program produced.
"""


# What is wrong with names.txt  (found by reading it, not by guessing):
# 1. Check whether there are empty lines.
# 2. Check whether some names have extra spaces.
# 3. Check whether capitalization is inconsistent.
# 4. Check whether there are duplicate or invalid names.
# Replace these comments with the problems actually found.

# 1. In:
# The input is names.txt, which contains a list of names.

# 2. Process, problem by problem:
# - Remove empty lines.
# - Remove unnecessary spaces between words.
# - Fix capitalization using title().
# - Remove duplicate names.
# - Skip entries containing numbers or fewer than two words.
# - Sort the names alphabetically by last name.

# 3. Out:
# The output is cleaned_names.txt.
# The original names.txt will not be changed.

# 4. How I decide which word is the last name:
# I assume the last word is the last name.
# For example, in "John Smith", "Smith" is the last name.
# I sort alphabetically using that word.


# Your code below

# Step 1: Read the original file
with open("names.txt", "r", encoding="utf-8-sig") as file:
    lines = file.readlines()

print("Original number of lines:", len(lines))


# Step 2: Clean the names
cleaned_names = []
seen = set()

empty_count = 0
duplicate_count = 0
invalid_count = 0

for line in lines:

    # Remove unnecessary spaces
    name = " ".join(line.strip().split())

    # Skip empty lines
    if name == "":
        empty_count += 1
        continue

    # Skip invalid entries
    if len(name.split()) < 2 or any(c.isdigit() for c in name):
        invalid_count += 1
        continue

    # Fix capitalization
    name = name.title()

    # Remove duplicate names
    if name.lower() in seen:
        duplicate_count += 1
        continue

    seen.add(name.lower())
    cleaned_names.append(name)


# Step 3: Sort alphabetically by last name
cleaned_names.sort(key=lambda name: name.split()[-1].lower())


# Step 4: Save the cleaned names into a new file
with open("cleaned_names.txt", "w", encoding="utf-8") as file:
    for name in cleaned_names:
        file.write(name + "\n")


# Step 5: Check the result
print("\nCleaning completed!")
print("Original lines:", len(lines))
print("Empty lines removed:", empty_count)
print("Duplicates removed:", duplicate_count)
print("Invalid entries removed:", invalid_count)
print("Final number of names:", len(cleaned_names))

if cleaned_names:
    print("First name in sorted list:", cleaned_names[0])
    print("Last name in sorted list:", cleaned_names[-1])

print("\nFile saved as cleaned_names.txt")
print("Original names.txt was not modified.")