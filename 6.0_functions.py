"""Exercise 6.0 — Naming a piece of work

WHAT THE PROGRAM MUST DO
    Write a function that computes something useful about the list you built in exercise
    4.0, then call it three times with different inputs and display the three results.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?  (what your function receives)
    2. What happens to it?
    3. What comes out?  (what your function returns)
    4. What is your function called, and does its name say what it does without reading
       the code?

WHAT THE AI CANNOT KNOW
    What is worth computing about your data, and what to call it. A function named
    "process" or "do_stuff" fails this exercise even if it works.

    Your function must RETURN its result, not print it. Find out why that difference
    matters and write the reason in a comment. It is the whole point of the exercise.

CHECK IT YOURSELF
    Call your function with an empty list. Note what happens. Then decide whether that
    behaviour is acceptable, and say so in a comment.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: Two numbers to be added together.
# 2. Process: The function adds num1 and num2.
# 3. Out: The sum of the two numbers.
# 4. My function name, and why return rather than print:
# The function is called add_numbers. It describes the calculation.
# Return allows the result to be stored and reused.
# An empty list returns 0 using default values.


# Your code below
number_1 = 10
number_2 = 20

# Define the function
def add_numbers(num1=0, num2=0):
    sum_result = num1 + num2
    return sum_result

# First call
result1 = add_numbers(number_1, number_2)
print("The sum of", number_1, "and", number_2, "is", result1)

# Second call
result2 = add_numbers(30, 40)
print("The second result is:", result2)

# Third call
result3 = add_numbers(50, 60)
print("The third result is:", result3)

# Test with an empty list
empty_list = []
print("Empty list result:", add_numbers(*empty_list))