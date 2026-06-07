'''This graphical user interface program is made for the school cafe. 
The school cafe wants a user-friendly menu-driven program for a cafe 
order click and collect app to be created. The program is meant to 
display a list of products and prices, allow users to login and place 
orders and then provide an order invoice relevant details, all through
a graphical user interface (easygui) with functions accompanying for
organisation and efficiency.'''

# Modules
import easygui    # import easygui module so easygui functions can be used in program (e.g. easygui.msgbox(), easygui.enterbox(), etc.)
import sys        # import sys module so sys functions can be used in program (e.g. sys.exit())
import math       # import math module to calculate total price of order, etc.

# Declaring constants
YR_LVL = range(9, 14)

# Declaring global variables
food_menu_items = {
        "  -> Eggs Benedict Deluxe       -   $17.50" : 17.50,
        "  -> Custom Omelette            -   $17.50" : 17.50,
        "  -> Omelette                   -   $15.20" : 15.20,
        "  -> Scrambled Eggs             -   $15.00" : 15.00,
        "  -> Poached Eggs               -   $12.90" : 12.90,
        "  -> French Toast + Butter      -    $9.60" : 9.60,
        "         * berries, banana, maple syrup          -   +$2.00ea" : 2.00,
        "  -> Cheesy Garlic Bread        -    $4.00" : 4.00,
        "  -> Cheese Toastie             -    $3.90" : 3.90,
        "  -> Mushroom Toastie           -    $3.90" : 3.90,
        "  -> Smashed Avocado Toast      -    $3.90" : 3.90,
        "  -> Buttermilk Pancakes        -   $13.50" : 13.50,
        "         * berries, molten chocolate, ice cream  -   +$2.00ea" : 2.00,
        "  -> Nutella Pancakes           -   $12.80" : 12.80,
        "  -> Double Choc Pancakes       -   $12.00" : 12.00,
        "  -> Avocado + Chicken Burger   -   $10.20" : 10.20,
        "  -> Vege Pea Protein Burger    -    $9.70" : 9.70,
        "  -> English Muffin Cheese Melt -    $6.10" : 6.10,
        "  -> Creamy Chicken Alfredo     -   $13.60" : 13.60,
        "         * GF pasta                              -   +$1.30ea" : 1.30,
        "  -> Meatballs Marinara         -   $13.20" : 13.20,
        "  -> Pesto Pasta                -   $12.90" : 12.90,
        "  -> Mac N' Cheese              -    $9.90" : 9.90
    }

order = {}  # empty dictionary to store user's order details

# Menu Function
def order_menu():
    message = "Please select your items"
    title4 = "BDSC School Cafe - All Day Food Menu"
    chosen = easygui.choicebox(message, title4, list(food_menu_items.keys()))
    if chosen:
        for item in chosen:
            order[item] = food_menu_items[item]

# Function to calculate total price of order
def calculate_total_price(order):
    return(math.fsum(order.values()))   # using math to carry out math.fsum() so that total price of order can be calculated through addition

# Welcoming user
welcome = "Welcome to BDSC School Cafe Click and Collect!"   # informs user of the name of the app and warmly welcomes the user to it.
title1 = "Welcome Page"
easygui.msgbox(welcome, title1) # printing welcome messagebox to user

# Asking if user wishes to proceed
proceed = "BDSC School Cafe Click and Collect will need you to enter some of your details.\nDo you wish to continue?"
title2 = "Permission to Ask User Details"
choices = ["Yes. Login into platform", "No. Exit out of platform."]
reply = easygui.choicebox(proceed, title2, choices)    # using choicebox to ask user which option they want to choose (login or exit)

if reply == choices[0]:    # using indexing to determine which option user chose
    # If "Yes. Login into platform" is chosen:
    easygui.msgbox("Okay. Lets continue on to the login page!")

elif reply == choices[1]:
    # If "No. Exit out of platform." is chosen:
    sys.exit(easygui.msgbox("Goodbye! Come back soon to use BDSC School Cafe Click and Collect!"))

else:
    # If user closes or cancels the dialog box by accident:
    sys.exit(easygui.msgbox("Oh no! You cancelled or closed the dialog box.\nPlease restart BDSC School Cafe Click and Collect platform."))


# Asking user details
# Asking name details
while True:
    name = easygui.enterbox("Enter your name: ")    # using enterbox so user can enter their name
    if name.isalpha():    # using isalpha() to check if name only contains letters
        easygui.msgbox(f"Hi {name}!!")   # greeting user by their name
        break
    else:
        easygui.msgbox("Invalid input. Please enter only letters for your name.")

# Asking year level details
while True:
    yr_lvl = easygui.integerbox("Enter your year level: ")   # using integerbox so user can enter their year level as an integer
    if yr_lvl in YR_LVL:   # using 'in' operator to check if year level is within the range of 9-13
        easygui.msgbox(f"Great! Since you are in year {yr_lvl},\nyou may continue on in using the BDSC School Cafe Click and Collect!")   # confirming user's year level
        break   # breaks loop if a valid year level is entered
    else:
        easygui.msgbox("Invalid input. Please enter a year level between 9 and 13.")  # exceeds boundaries of year level range

def display_main_menu():
    while True:
        main_menu = "Would you like to order from the cafe menu?"
        title3 = "Main Menu"
        choices = ["Yes. Show me the menu!", "No. Exit out of platform."]
        reply = easygui.choicebox(main_menu, title3, choices)    # using choicebox to ask user if they want to see the cafe menu or exit
        
        if reply == choices[0]:
            order_menu()

        elif reply == choices[1]:
            sys.exit(easygui.msgbox("Sad to see you go! Come back soon!"))
        
        else:
            sys.exit(easygui.msgbox("Oh no! You cancelled or closed the dialog box.\nPlease restart BDSC School Cafe Click and Collect platform."))

display_main_menu()