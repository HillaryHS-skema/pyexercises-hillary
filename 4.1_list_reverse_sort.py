"""Exercise 4.1 — Reordering without losing the original (homework)

WHAT THE PROGRAM MUST DO
    Starting from the list you built in exercise 4.0, display it in four different
    orders, and prove at the end that the original list has not been damaged.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which four orders did you choose, and in which of them is your original list
       modified rather than copied?

WHAT THE AI CANNOT KNOW
    That your original must survive. Some ways of reordering a list change it in place,
    others return a new one. Find out which is which, and say so in your comments.
    That distinction is the entire exercise.

CHECK IT YOURSELF
    The last line of your program must display the original list. Compare it, item by
    item, with what you wrote in 4.0. If it has moved, your program is wrong even
    though it ran.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: A list of 8 monthly marketing budgets for a fashion brand.
# 2. Process: The program displays the budgets in four different orders without changing the original list.
# 3. Out: The original list, ascending order, descending order, reversed order, and the unchanged original list.
# 4. My four orders, and which ones modify the original: 
# Original order: displays the list without changing it.
# Ascending order: sorted() creates a new sorted list.
# Descending order: sorted(reverse=True) creates a new list.
# Reversed order: [::-1] creates a reversed copy.
# None of these operations modify the original list.


# Your code below

# List from Exercise 4.0
budgets = [1200, 2500, 800, 3000, 1500, 2200, 950, 1800]

# Save a copy to check that the original is unchanged
original = budgets.copy()

# 1. Display the original order
print("Original order:", budgets)

# 2. Sort from smallest to largest
ascending = sorted(budgets)
print("Ascending order:", ascending)

# 3. Sort from largest to smallest
descending = sorted(budgets, reverse=True)
print("Descending order:", descending)

# 4. Reverse the original order
reversed_list = budgets[::-1]
print("Reversed order:", reversed_list)

# Check if the original list is unchanged
print("Original list unchanged:", budgets == original)

# Display the original list again (must be the last line)
print("Original list at the end:", budgets)