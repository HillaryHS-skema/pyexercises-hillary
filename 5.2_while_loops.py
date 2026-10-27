"""Exercise 5.2 — Repeating until something changes

WHAT THE PROGRAM MUST DO
    Keep asking the user something until a condition you define is met, then display a
    summary of what happened during the loop.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What is your stop condition, what is your maximum number of attempts, and what
       does your summary contain?

WHAT THE AI CANNOT KNOW
    Your stop condition and your safety limit. An assistant asked for a while loop will
    write one that can run for ever if the user never gives the expected answer. Decide
    how many attempts you allow, and what your program does when that limit is reached.

    Accepting "Yes", "yes" and " yes " as the same answer is your decision too. Make it
    and write it down.

CHECK IT YOURSELF
    Run it and never give the expected answer. If your program is still running after
    your stated maximum, it is wrong. Then run it and answer with capitals and extra
    spaces.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: User answers yes or no to adding a marketing campaign.
# 2. Process: A while loop keeps asking the user. Each answer is checked and counted.
# The loop stops when the user says no or reaches the maximum number of attempts.
# 3. Out:The program displays the number of campaigns added, total attempts, and why the loop stopped.
# 4. My stop condition, my attempt limit, my summary:
# The loop stops when the user enters "no" or after 5 attempts.
# I accept YES, Yes, yes, and extra spaces. Invalid answers count as attempts.
# The summary shows campaigns added, attempts used, and the reason the loop stopped.



# Your code below

attempts = 0
campaigns = 0
max_attempts = 5
reason = "Maximum attempts reached"

while attempts < max_attempts:

    answer = input("Add another marketing campaign? (yes/no): ").strip().lower()
    attempts += 1

    if answer == "yes":
        campaigns += 1
        print("Campaign added!")

    elif answer == "no":
        print("You chose to stop.")
        reason = "User entered no"
        break

    else:
        print("Invalid input. Please enter yes or no.")

# Summary after the loop
print("The loop has finished.")
print("Total attempts:", attempts)
print("Campaigns added:", campaigns)
print("Reason for stopping:", reason)
