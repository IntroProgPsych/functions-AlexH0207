# https://www.w3schools.com/python/python_strings_format.asp
# Write a function greet_person(name) that returns the message “Hello, NAME!”.
# Ask the user for their name and print the returned message.
    
# Write your code here:

def greet_person(name):
    return f"Hello, {name}!"
name=input("What is your name? ")
print(greet_person(name))