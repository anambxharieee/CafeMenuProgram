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

# Declaring constants
YR_LVL = range(9, 14)

# Declaring global variables
menu_items = {
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
        "  -> Mac N' Cheese              -    $9.90" : 9.90,
        "  -> Mango Smoothie             -    $6.20" : 6.20,
        "  -> Mixed Berry Smoothie       -    $6.20" : 6.20,
        "  -> Lime Tropical Smoothie     -    $6.20" : 6.20,
        "  -> Apple Juice                -    $3.60" : 3.60,
        "  -> Orange Juice               -    $3.60" : 3.60,
        "  -> Mango + Orange Juice       -    $3.60" : 3.60,
        "  -> Tropical Juice             -    $3.60" : 3.60,
        "  -> Aloe Vera                  -    $4.20" : 4.20,
        "  -> Iced Coffee                -    $5.50" : 5.50,
        "  -> Iced Chocolate             -    $4.90" : 4.90,
        "  -> Chai Latte                 -    $5.20" : 5.20,
        "  -> Matcha Latte               -    $6.10" : 6.10,
        "  -> Cappuccino                 -    $7.20" : 7.20,
        "  -> Espresso                   -    $7.50" : 7.50,
        "  -> Flat White                 -    $6.30" : 6.30,
        "  -> Americano                  -    $6.80" : 6.80,
        "  -> Mocha                      -    $6.40" : 6.40,
        "  -> Hot Chocolate              -    $5.90" : 5.90,
        "      * DELUXE: 4 pumps of molten chocolate     -    +$1.50ea" : 1.50,
        "      * STANDARD: 2 pumps of molten chocolate   -    +$0.50ea" : 0.50,
        "  -> Tea                        -    $3.30" : 3.30
    }

order = {}     # empty dictionary to store user's order details

# Declaring All Functions
# Menu Function
def order_menu():
    order.clear()   # resets order each time user orders
    message = "Please select your items"
    title4 = "BDSC School Cafe - All Day Food Menu"
    chosen = easygui.multchoicebox(message, title4, list(menu_items.keys()))
    if chosen:
        for item in chosen:
            order[item] = menu_items[item]

def invoice():
    def calculate_subtotal_price():    # Function to calculate subtotal price of order (before gst)
        subtotal_price = sum(order.values())
        return subtotal_price

    def calculate_total_price():     # Function to calculate total price of order (after gst)
        gst = calculate_subtotal_price() * 0.15
        total_price = calculate_subtotal_price() + gst
        return total_price
    
    order_list = ""     # empty string to store user's ordered items in
    for item in order.keys():
        order_list += f"{item}\n"    # '+=' adds item to string on a brand new line

    order_invoice = ("===================================================\n"
                     "                   Order Invoice                   \n"
                     "===================================================\n"
                     f"Name:                                       {name}\n"
                     f"Year Level:                                    {yr_lvl}\n"
                     F"Pick Up Time:                         {time}\n"
                     "---------------------------------------------------\n"
                     f"Order:\n{order_list}"
                     "---------------------------------------------------\n"
                     f"Subtotal Price:          $ {calculate_subtotal_price():.2f}\n"
                     f"GST (15%):               $ {calculate_subtotal_price() * 0.15:.2f}\n"
                     f"Total Price:             $ {calculate_total_price():.2f}\n"
                     )
    easygui.codebox("Please see your Order Invoice below:", "Invoice Receipt", order_invoice)

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
    
    # If user's year level is in range
    if yr_lvl in YR_LVL:   # using 'in' to check if year level is within the range of 9-13
        easygui.msgbox(f"Thank you {name} for entering your user details.\nYour request in using the BDSC School Cafe Click and Collect is approved!")   # confirming user's year level
        break   # breaks loop if a valid year level is entered

    # If user's year level is NOT in range
    elif yr_lvl != range(9,14):
        sys.exit(easygui.msgbox(f"Sorry {name}, you are not able to use the BDSC Cafe Click and Collect.\nSadly, you do not fit the year level range (9-13) requirements."))  # exceeds boundaries of year level range

    # If user closes or cancels the dialog box by accident:
    else:
        sys.exit(easygui.msgbox("Oh no! You cancelled or closed the dialog box.\nPlease restart BDSC School Cafe Click and Collect platform."))

# Asking user what time they would like to pick up their order
pickup_time = "What time would you like to pick up your order?"
title5 = "Order Pick Up Time"
time_choices = ["Before School", "Morning Tea", "Lunch", "After School"]
time = easygui.choicebox(pickup_time, title5, time_choices)

# If user picks a time for order pick up
if time_choices:
    easygui.msgbox(f"Thank you {name} for clarifying when you will be able to pick up your order.")

# If user closes or cancels the dialog box by accident:
else:
    sys.exit(easygui.msgbox("Oh no! You cancelled or closed the dialog box.\nPlease restart BDSC School Cafe Click and Collect platform."))
        

# Order Main Menu
def display_main_menu():
    while True:
        main_menu = "Would you like to order from the cafe menu?"
        title3 = "Main Menu"
        choices = ["Yes. Show me the menu!", "No. Exit out of platform."]
        reply = easygui.choicebox(main_menu, title3, choices)    # using choicebox to ask user if they want to see the cafe menu or exit
        
        if reply == choices[0]:
            order_menu()
            invoice()


        elif reply == choices[1]:
            sys.exit(easygui.msgbox("Sad to see you go! Come back soon!"))
        
        else:
            sys.exit(easygui.msgbox("Oh no! You cancelled or closed the dialog box.\nPlease restart BDSC School Cafe Click and Collect platform."))

display_main_menu()