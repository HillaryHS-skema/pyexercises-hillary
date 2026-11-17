"""Exercise 9.0 — Surviving what you did not expect

Useful for the final exam: two campaigns in the exam dataset have zero conversions.

WHAT THE PROGRAM MUST DO
    Ask the user for a number, divide something by it, and keep running whatever the
    user types. Never crash.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which two different failures can happen here, and should they produce the same
       message to the user? Decide before coding.

WHAT THE AI CANNOT KNOW
    Your answer to question 4, and how many attempts you allow before giving up.

    An assistant will often propose catching every error at once. Find out why catching
    each failure separately is better, and write the reason in a comment.

CHECK IT YOURSELF
    Run it with: a normal number, then zero, then the word "abc", then an empty line.
    Four runs, four behaviours, all described in a comment. If any of them stopped your
    program, it is not finished.

DELIVERABLE
    This file, with your comments and your code.
"""

"""
Exercise 9.0 — Surviving what you did not expect
"""

# 1. In:
# The user enters the number of conversions for a marketing campaign.
# The campaign has a total budget of 1000 euros.

# 2. Process:
# The program divides the campaign budget by the number of conversions.
# It uses try and except to handle errors.
# The user has a maximum of 4 attempts.
# If the input is invalid, the program explains the problem
# and allows the user to try again.

# 3. Out:
# The program displays the cost per conversion in euros.
# If the input is invalid, it displays an error message.
# After 4 unsuccessful attempts, the program ends normally.

# 4. The two failures, and whether they deserve the same message:
# Failure 1: ZeroDivisionError happens when the user enters 0.
# Failure 2: ValueError happens when the user enters text
# such as "abc" or leaves the input empty.
# These errors should have different messages because
# the reasons for failure are different.
# Catching them separately helps the user understand
# what went wrong and how to fix it.

# CHECK IT YOURSELF:
# Normal number (e.g. 10): Displays 100.00 euros per conversion.
# Zero (0): Displays a warning about division by zero.
# Text ("abc"): Displays a warning to enter a valid number.
# Empty input (""): Displays a warning to enter a valid number.
# None of these inputs cause the program to crash.


# Your code below

# Step 1: Define campaign budget
budget = 1000

print("EXERCISE 9.0 — ERROR HANDLING")
print("Fashion Marketing Campaign")
print("Campaign budget: 1000 EUR")
print("-" * 40)

# Step 2: Set maximum number of attempts
max_attempts = 4

# Step 3: Ask the user for conversions
for attempt in range(1, max_attempts + 1):

    print(f"\nAttempt {attempt} of {max_attempts}")

    try:
        conversions = float(input("Enter number of conversions: "))

        # Calculate cost per conversion
        cost_per_conversion = budget / conversions

    except ValueError:
        print("Error: Please enter a valid number.")

    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
        print("The campaign must have more than 0 conversions.")

    else:
        print("\nCalculation successful!")
        print(f"Cost per conversion: {cost_per_conversion:.2f} EUR")
        break

else:
    print("\nMaximum attempts reached.")
    print("The program has ended safely.")

print("\nThank you for using the program!")