"""Exercise 5.1 — Doing the same thing to every item

WHAT THE PROGRAM MUST DO
    Take the list you built in exercise 4.0 and, for every item, display a line that
    combines the item, its position, and something computed about it.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What did you compute for each item, and what does the reader learn from that line?

WHAT THE AI CANNOT KNOW
    Your list from 4.0, and what is worth computing about its items. Length of the name,
    share of a total, position in a ranking, whether the item passes a threshold you set.
    Open your 4.0 file, copy the list across, and say in a comment what you decided.

CHECK IT YOURSELF
    Count the lines your program printed. There must be exactly as many as items in your
    list. If there is one more or one less, you have an off-by-one, and it is worth
    understanding now rather than in the exam.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: A list of 8 monthly marketing budgets for a fashion brand.
# 2. Process: Use a for loop to go through each budget, find its position, and calculate its percentage of the total marketing budget.
# 3. Out: Each budget, its position in the list, and its percentage of the total budget.
# 4. What I compute for each item, and why it is worth showing:
# I calculate the percentage of the total budget represented by each marketing channel.
# This helps understand how a fashion brand distributes its marketing spending.


# Your code below

# List from Exercise 4.0
budgets = [1200, 2500, 800, 3000, 1500, 2200, 950, 1800]

# Calculate the total budget
total = sum(budgets)

# Use a for loop to go through each budget
for position, budget in enumerate(budgets):
    percentage = (budget / total) * 100

    print("The budget is:", budget,
          "its position is:", position,
          "and its percentage of the total is:",
          round(percentage, 2), "%")
