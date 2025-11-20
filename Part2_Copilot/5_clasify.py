# Write a function describe_number(n) that:

# returns “positive” if n > 0

# returns “zero” if n == 0

# returns “negative” if n < 0

# Ask the user for a number, call the function, and print the message.*

# Write your code here:

def describe_number(n):
    result=""
    if n==0: result="zero"
    elif n>0: result="positive"
    else: result="negative"
    return result
n=int(input("Number: "))
print(describe_number(n))