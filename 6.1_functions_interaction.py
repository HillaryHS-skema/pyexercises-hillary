"""Exercise 6.1 — Small functions working together

WHAT THE PROGRAM MUST DO
    Write three small functions, each doing one thing, and a fourth that uses the other
    three to answer one question about your data.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?  (say which function does what, in order)
    3. What comes out?
    4. What question does your fourth function answer, and why does splitting it into
       three make it easier to check?

WHAT THE AI CANNOT KNOW
    Your question and your split. Ask an assistant for "three functions" and it will
    invent three; they will not be the three your question needs. Decide the split first,
    on paper, then ask.

    One function, one job. If you cannot describe what one of yours does in a single
    sentence without using the word "and", it is doing two things.

CHECK IT YOURSELF
    Test each of the three small functions on its own before combining them. Write in a
    comment the input and expected output you used for each. That is three test cases,
    and they are part of the deliverable.

DELIVERABLE
    This file, with your comments and your code.
"""


# 1. In:
# Four numbers entered into the program.

# 2. Process, function by function:
# is_zero checks if the number equals 0.
# is_even checks if the number is even.
# is_positive checks if the number is greater than 0.
# check_number uses all three functions to determine
# whether each number is positive, negative, or zero,
# and whether it is odd or even.

# 3. Out:
# Four results describing the numbers.

# 4. The question my fourth function answers:
# Is the number positive, negative, or zero?
# Is it odd or even?
# Splitting the program into three functions makes
# each condition easier to test separately.


# Your code below

number_1 = 10
number_2 = -5
number_3 = 0
number_4 = 7

# Function 1: Check if zero
def is_zero(num):
    return num == 0

# Function 2: Check if even
def is_even(num):
    return num % 2 == 0

# Function 3: Check if positive
def is_positive(num):
    return num > 0

# Function 4: Combine all three functions
def check_number(num):
    zero = is_zero(num)
    even = is_even(num)
    positive = is_positive(num)

    if zero:
        return "The number is zero"
    elif positive and even:
        return "The number is positive and even"
    elif positive:
        return "The number is positive and odd"
    elif even:
        return "The number is negative and even"
    else:
        return "The number is negative and odd"


# Test each function separately

# Test 1: Input 0, expected output True
assert is_zero(0) == True

# Test 2: Input 10, expected output True
assert is_even(10) == True

# Test 3: Input 10, expected output True
assert is_positive(10) == True


# Call the fourth function four times
result1 = check_number(number_1)
result2 = check_number(number_2)
result3 = check_number(number_3)
result4 = check_number(number_4)

# Display the results
print(result1)
print(result2)
print(result3)
print(result4)