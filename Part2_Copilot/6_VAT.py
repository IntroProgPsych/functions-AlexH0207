# Write a function apply_vat(price) that returns the price including 19% VAT.
# Ask the user for a price and print the result.

# Write your code here:

def apply_vat(price):
    return price + price*0.19

price=int(input("price: "))
print(apply_vat(price))