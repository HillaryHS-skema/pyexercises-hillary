"""Exercise 8.1 — Bitwise operators (bonus, not graded)

WHAT THE PROGRAM MUST DO
    Represent a set of permissions as bits, combine two of them, test whether a third is
    present, then add it and remove one.

ANSWER THESE FIRST, in comments
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What are your permissions about? Not files: invent a set from your own field,
       such as who may view, edit and publish a campaign.

WHAT THE AI CANNOT KNOW
    Your permission set and what each one means in your context.

CHECK IT YOURSELF
    Display the value in binary at each step and read the bits yourself.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. What goes in?
# Four marketing campaign permissions represented by binary bits:
# VIEW = 0001, EDIT = 0010, APPROVE = 0100, PUBLISH = 1000.

# 2. What happens to it?
# - Combine VIEW and EDIT using the bitwise OR operator (|).
# - Check whether PUBLISH is present using bitwise AND (&).
# - Add PUBLISH using bitwise OR (|).
# - Remove EDIT using bitwise AND (&) and NOT (~).
# - Display the permissions in binary after each step.

# 3. What comes out?
# The program displays the permissions and their binary values.
# It also shows whether PUBLISH permission is present.
# The final permissions are VIEW and PUBLISH.

# 4. What are my permissions about?
# My permissions are for managing a fashion marketing campaign.
# VIEW means someone can see the campaign.
# EDIT means someone can change the campaign content.
# APPROVE means someone can approve the campaign.
# PUBLISH means someone can publish the campaign online.


# Your code below

# Step 1: Define the permissions
VIEW = 0b0001
EDIT = 0b0010
APPROVE = 0b0100
PUBLISH = 0b1000

print("EXERCISE 8.1 — BITWISE OPERATORS")
print("\nFASHION MARKETING CAMPAIGN PERMISSIONS")
print("-" * 40)

print("VIEW:   ", format(VIEW, "04b"))
print("EDIT:   ", format(EDIT, "04b"))
print("APPROVE:", format(APPROVE, "04b"))
print("PUBLISH:", format(PUBLISH, "04b"))


# Step 2: Combine VIEW and EDIT permissions
permissions = VIEW | EDIT

print("\nSTEP 1: COMBINE VIEW AND EDIT")
print("Permissions:", format(permissions, "04b"))


# Step 3: Check if PUBLISH permission is present
has_publish = (permissions & PUBLISH) != 0

print("\nSTEP 2: CHECK PUBLISH PERMISSION")
print("Current permissions:", format(permissions, "04b"))
print("Can publish?", has_publish)


# Step 4: Add PUBLISH permission
permissions = permissions | PUBLISH

print("\nSTEP 3: ADD PUBLISH PERMISSION")
print("New permissions:", format(permissions, "04b"))
print("Can publish?", (permissions & PUBLISH) != 0)


# Step 5: Remove EDIT permission
permissions = permissions & ~EDIT

print("\nSTEP 4: REMOVE EDIT PERMISSION")
print("New permissions:", format(permissions, "04b"))


# Step 6: Display final permissions
print("\nFINAL PERMISSIONS")
print("-" * 40)

print("VIEW:", (permissions & VIEW) != 0)
print("EDIT:", (permissions & EDIT) != 0)
print("APPROVE:", (permissions & APPROVE) != 0)
print("PUBLISH:", (permissions & PUBLISH) != 0)

print("\nFinal binary value:", format(permissions, "04b"))
print("\nExercise completed!")