"""Exercise 4.2 — Working with a dictionary

WHAT THE PROGRAM MUST DO
    Describe one real object from your field using a dictionary of at least five fields,
    then read it, change it, remove one field, and display every field with its value.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What object did you describe, which five fields did you choose, and why those?
       A field you would never actually use does not count.

WHAT THE AI CANNOT KNOW
    Your object and your fields. A campaign, a customer, a product, a store, a supplier.
    Choose something you would genuinely have to describe in your job.

CHECK IT YOURSELF
    Ask your program for a field that does not exist. Note what happens in a comment,
    then make it survive that case.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: Information about a luxury fashion handbag, including its name, brand, category, price, and stock quantity.
# 2. Process: Create a dictionary, display its information, update the price, remove the stock field, and check for a missing field.
# 3. Out: The original product information, updated price, removed stock value, and remaining product details.
# 4. My object, my five fields, and why those: My object is a luxury handbag. I chose name, brand, category, price, and stock
# because these are important for product management, pricing, and inventory tracking in the fashion industry.



# Your code below

# Create a dictionary for a luxury fashion product
product = {
    "name": "Leather Handbag",
    "brand": "Loewe",
    "category": "Handbag",
    "price": 2500,
    "stock": 15
}

# Print the dictionary
print("Product dictionary:", product)

# Read one field from the dictionary
print("Product name:", product["name"])

# Update the price field
product["price"] = 2300

# Print the updated dictionary
print("Updated product dictionary:", product)

# Remove the stock field
stock = product.pop("stock")

# Print the dictionary after removing stock
print("Product dictionary after removing stock:", product)
print("Removed stock:", stock)

# Display every field and its value
for key, value in product.items():
    print(key, ":", value)

print("Product color:", product.get("color", "Not available"))
