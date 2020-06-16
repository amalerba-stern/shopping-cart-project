# shopping_cart.py

import datetime

products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50, "price_per": "item"},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99, "price_per": "item"},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49, "price_per": "item"},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99, "price_per": "item"},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99, "price_per": "item"},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99, "price_per": "item"},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50, "price_per": "item"},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25, "price_per": "item"},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50, "price_per": "item"},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99, "price_per": "item"},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99, "price_per": "item"},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50, "price_per": "item"},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00, "price_per": "item"},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99, "price_per": "item"},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50, "price_per": "item"},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50, "price_per": "item"},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99, "price_per": "item"},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50, "price_per": "item"},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99, "price_per": "item"},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25, "price_per": "item"},
    {"id":21, "name": "Bananas", "department": "grocery", "aisle": "fruit", "price": 0.79, "price_per": "pound"}
] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017

def to_usd(my_price):
    """
    Converts a numeric value to usd-formatted string, for printing and display purposes.
    Param: my_price (int or float) like 4000.444444
    Example: to_usd(4000.444444)
    Returns: $4,000.44
    """
    return f"${my_price:,.2f}" #> $12,000.71

# TODO: write some Python code here to produce the desired output

products_ids = [product["id"] for product in products]
first_id = products_ids[0]
last_id = products_ids[-1]
error_msg = f"This is not a valid input. A product id must be a number between {first_id} and {last_id}."
shopping_cart = []
x = None

# Get product IDs as inputs
# Allow user to continue adding items until they type "DONE"
while True:
    x = input(f"Please input a product identifier ({first_id}-{last_id}):")
    if x == "DONE":
        break
    try:
        if int(x) not in products_ids:
            print(error_msg)
            continue
    except ValueError:
        print(error_msg)
    else:
        shopping_cart.append(int(x))

store_name = "Great Groceries"
store_phone_number = "212-555-1234"
store_address = "15 W 15th St. New York, NY"
store_website = "greatgroceries.com"

print("----------------------")
print(store_name.upper())
print("----------------------")
print(store_phone_number)
print(store_address)
print(store_website)
print("----------------------")
checkout_time = datetime.datetime.now()
print("CHECKOUT AT:", checkout_time.strftime("%Y-%m-%d %I:%M %p"))
print("----------------------")

running_total = []

print("YOUR SELECTED ITEMS:")
for item in shopping_cart:
    name = [product["name"] for product in products if product["id"] == item][0]
    price_per = [product["price_per"] for product in products if product["id"] == item][0]
    if price_per == "item":
        price = [product["price"] for product in products if product["id"] == item][0]
    elif price_per == "pound":
        lbs = input(f"How many pounds of {name} did you buy?")
        price_lb = [product["price"] for product in products if product["id"] == item][0]
        price = float(lbs) * price_lb
    running_total.append(price)
    print(f"...{name} ({to_usd(price)})")

print("----------------------")
subtotal = sum(running_total)
print("SUBTOTAL:", to_usd(subtotal))
sales_tax_rate_nyc = 0.0875
sales_tax = subtotal * sales_tax_rate_nyc
print("SALES TAX:", to_usd(sales_tax))
total = subtotal + sales_tax
print("TOTAL:", to_usd(total))

print("----------------------")
print("Thank you for shopping here today!")
print("We hope to see you again soon.")