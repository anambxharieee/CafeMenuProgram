'''This program is being made for the school cafe. 
The school cafe wants a menu-driven program for a 
cafe order click and collect app to be created. 
The program is meant to display a list of products 
and prices, allow users to login and place orders 
and then provide an order invoice relevant details.'''

# Modules
import math # import math module so math functions can be used in program
import sys # import sys module so sys functions can be used in program


# Declaring constants
YR_LVL = range(9, 14)

# This is the main menu of the cafe order click and collect app
print("Welcome to the School Cafe Click and Collect!") # User welcome message
login = input("Do you want to login? (yes/no): ")      # Login prompt (yes or no)
if login.lower() == "yes":
    while True:
        try:
            # User login details
            user_name = input("Enter your name: ")     # Name input prompt
            if user_name == user_name.strip():
                print("Name is valid.")
            break
        except NameError:
            print("Invalid input. Please only use letters.")

    while True:
        try:
            age = input("Enter your age: ")         # Age input prompt

            if age == age.isnumeric():
                print("Age is valid.")
            break
        except ValueError:
            print("Invalid input. Please enter a numeric age.")
    
    while True:
        try:
            yr_level = int(input("Enter your year level: "))    # year level input prompt
            if yr_level in YR_LVL:
                print("Login successful!")
                break
            else:
                sys.exit("")
        except ValueError:
            print("Invalid input. Please enter only numeric values.")
    
    print("Here is the menu:")
    options = {"Sandwich": "$5.00",
                  "Wrap": "$6.00",
                  "Salad": "$4.00",
                  "Chicken Nuggets": "$5.50",
                  "Fruit": "$2.00",
                  "Soft Drink": "$1.50"}
    
    print(options)
    order = input("What would you like to order? ")
    for item in options:
        if order in item:
            print(f"You have ordered {order} for {item[order]}.")
            break

else:
    exit = print("Thank you for using BDSC School Cafe Click and Collect. Come back soon, have a great day!")