"""Exercise 10.0 — Checking the shape of text (bonus, not graded)

WHAT THE PROGRAM MUST DO
    Validate three pieces of information typed by the user, and only save them when all
    three are acceptable.

ANSWER THESE FIRST, in comments
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What are your three fields, and what makes a value acceptable for each? Write the
       rule in plain English before writing any pattern.

WHAT THE AI CANNOT KNOW
    Your three rules. "A valid email" is not a rule, it is a wish. Say what you accept
    and what you reject, and be ready to defend a borderline case.

WHAT TO WATCH
    An assistant will hand you a pattern that looks like line noise. Do not accept it
    until it has explained it to you piece by piece, and you have written that
    explanation in your own words above it.

CHECK IT YOURSELF
    For each field, prepare one value that must pass and two that must fail. Run all
    nine. Any surprise goes in a comment.

DELIVERABLE
    This file, with your comments and your code.
"""


# 1. What goes in?
# The user enters three pieces of information:
# - A fashion marketing campaign code
# - An Instagram username
# - A campaign launch date

# 2. What happens to it?
# The program checks each value using regular expressions.
# It checks whether each input follows the required format.
# It also checks whether the launch date actually exists.
# If all three values are valid, they are saved to a CSV file.
# If any value is invalid, nothing is saved.

# 3. What comes out?
# The program displays whether each value is valid.
# If all three are valid, the information is saved to
# campaign_entries.csv.
# Otherwise, the program displays an error message.

# 4. What are my three fields and their rules?
#
# Field 1: Campaign Code
# Must start with "CAM-", followed by exactly 3 uppercase
# letters, a hyphen, and 2 numbers.
# Accepted: CAM-LUX-26
# Rejected: CAM-lux-26, LUX-26
#
# Pattern explanation:
# CAM- means the text must start with CAM-
# [A-Z]{3} means exactly 3 uppercase letters
# - means a hyphen
# [0-9]{2} means exactly 2 digits
#
# Field 2: Instagram Username
# Must start with @ followed by 3 to 15 characters.
# The first character after @ must be a lowercase letter.
# The remaining characters can be lowercase letters,
# numbers, or underscores.
# Accepted: @fashion_team
# Rejected: @ab, @Fashion
#
# Pattern explanation:
# @ means the username must start with @
# [a-z] means the first character must be lowercase
# [a-z0-9_]{2,14} allows another 2 to 14 characters
#
# Field 3: Launch Date
# Must use YYYY-MM-DD format, with a year from 2000 to 2099.
# The date must also exist on the calendar.
# Accepted: 2026-12-05
# Rejected: 2026-02-30, 05/12/2026
#
# Pattern explanation:
# 20 means the year starts with 20
# [0-9]{2} means two more digits for the year
# - means a hyphen
# [0-9]{2} means exactly two digits for month or day
# datetime checks whether the date actually exists.
#
# Extra spaces at the beginning and end are removed
# before checking. Spaces inside values are not accepted.
#
# CHECK IT YOURSELF:
# Campaign code:
# CAM-LUX-26 = Pass
# CAM-lux-26 = Fail
# LUX-26 = Fail
#
# Instagram username:
# @fashion_team = Pass
# @ab = Fail
# @Fashion = Fail
#
# Launch date:
# 2026-12-05 = Pass
# 2026-02-30 = Fail (February does not have 30 days)
# 05/12/2026 = Fail (wrong date format)
#
# Nine tests in total: 3 pass and 6 fail.
# The test results are displayed before asking for input.


# Your code below

import re
import csv
from datetime import datetime
from pathlib import Path


# Step 1: Define the validation patterns

campaign_pattern = r"CAM-[A-Z]{3}-[0-9]{2}"
instagram_pattern = r"@[a-z][a-z0-9_]{2,14}"
date_pattern = r"20[0-9]{2}-[0-9]{2}-[0-9]{2}"


# Step 2: Create validation functions

def validate_campaign(value):
    value = value.strip()
    return re.fullmatch(campaign_pattern, value) is not None


def validate_instagram(value):
    value = value.strip()
    return re.fullmatch(instagram_pattern, value) is not None


def validate_date(value):
    value = value.strip()

    if re.fullmatch(date_pattern, value) is None:
        return False

    try:
        datetime.strptime(value, "%Y-%m-%d")
        return True
    except ValueError:
        return False


# Step 3: Test all nine examples

print("EXERCISE 10.0 — TEXT VALIDATION")
print("Fashion Marketing Campaign")
print("-" * 50)

tests = [
    ("Campaign", "CAM-LUX-26", True, validate_campaign),
    ("Campaign", "CAM-lux-26", False, validate_campaign),
    ("Campaign", "LUX-26", False, validate_campaign),

    ("Instagram", "@fashion_team", True, validate_instagram),
    ("Instagram", "@ab", False, validate_instagram),
    ("Instagram", "@Fashion", False, validate_instagram),

    ("Launch Date", "2026-12-05", True, validate_date),
    ("Launch Date", "2026-02-30", False, validate_date),
    ("Launch Date", "05/12/2026", False, validate_date)
]

correct = 0

print("\nVALIDATION TEST RESULTS")
print("-" * 65)

for field, value, expected, function in tests:
    result = function(value)

    if result == expected:
        status = "PASS"
        correct += 1
    else:
        status = "FAIL"

    print(f"{field:<14} {value:<20} "
          f"Valid: {str(result):<6} Test: {status}")

print("-" * 65)
print(f"Tests passed: {correct} out of {len(tests)}")


# Step 4: Ask the user for information

print("\nENTER YOUR CAMPAIGN INFORMATION")

campaign = input("Campaign code (CAM-XXX-00): ").strip()
instagram = input("Instagram username: ").strip()
launch_date = input("Launch date (YYYY-MM-DD): ").strip()


# Step 5: Validate all three fields

campaign_valid = validate_campaign(campaign)
instagram_valid = validate_instagram(instagram)
date_valid = validate_date(launch_date)

print("\nVALIDATION RESULTS")
print("-" * 40)

print("Campaign code valid:", campaign_valid)
print("Instagram username valid:", instagram_valid)
print("Launch date valid:", date_valid)


# Step 6: Save only if all three are valid

if campaign_valid and instagram_valid and date_valid:

    output_file = Path("campaign_entries.csv")

    # Check whether the file needs a header
    needs_header = (
        not output_file.exists()
        or output_file.stat().st_size == 0
    )

    with open(output_file, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        if needs_header:
            writer.writerow([
                "Campaign Code",
                "Instagram Username",
                "Launch Date"
            ])

        writer.writerow([
            campaign,
            instagram,
            launch_date
        ])

    print("\nAll information is valid!")
    print("Data successfully saved to campaign_entries.csv")

else:
    print("\nSome information is invalid.")
    print("No data was saved.")

    if not campaign_valid:
        print("- Campaign code must follow CAM-XXX-00.")

    if not instagram_valid:
        print("- Instagram username must start with @ and "
              "contain 3-15 allowed characters.")

    if not date_valid:
        print("- Launch date must be a real date in YYYY-MM-DD format.")


print("\nExercise completed!")