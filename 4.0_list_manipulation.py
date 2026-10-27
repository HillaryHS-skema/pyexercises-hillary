"""Exercise 4.0 — Working with a list

WHAT THE PROGRAM MUST DO
    Build a list of at least eight items, then display: the whole list, one item of your
    choice, the list sorted, and something computed from it.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What is your list about, and what did you compute from it? Why is that number
       interesting?

WHAT THE AI CANNOT KNOW
    The content of your list. It must come from your own field: marketing channels,
    campaign names, product references, cities you operate in, monthly budgets. Not
    fruit, not "item1, item2, item3".

    Keep this file. Exercise 5.1 and exercise 6.0 both reuse the list you build here.

CHECK IT YOURSELF
    If you computed an average, a total or a maximum, work it out by hand on three of
    your items first, then check your program agrees on those three.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: A list of 8 monthly marketing budgets for a fashion brand.
# 2. Process: The program displays, sorts, and modifies the list. It also calculates the total marketing budget.
# 3. Out: The original list, one selected budget, the sorted list, the total budget, and the list after removal.
# 4. What my list is about, and what I computed from it:  The list represents budgets for 8 marketing channels. I calculated the total to understand how much a fashion brand spends on marketing each month.


# Your code below

# Monthly marketing budgets in euros
# Instagram, TikTok, Pinterest, Google Ads, Email, Influencers, Events, SEO

budgets = [1200, 2500, 800, 3000, 1500, 2200, 950, 1800]

# Print the original list
print("List before sorting:", budgets)

# Print one item from the list
print("Instagram marketing budget:", budgets[0])

# Calculate the total marketing budget
total = sum(budgets)
print("Total monthly marketing budget:", total)

# Sort the list
budgets.sort()

# Print the sorted list
print("The sorted list is:", budgets)

# Remove the last item from the list
budgets.pop()

# Print list after removing the last item
print("The list after removing the last:", budgets)