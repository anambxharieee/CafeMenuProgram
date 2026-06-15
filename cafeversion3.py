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
YR_LVL = range(9, 14)    # students year level range
AGE = range(21, 71)      # teaching staff ages range

ALLOWED_EMAIL_DOMAINS = (      # email domains allowed in program
    "@gmail.com", 
    "@bdsc.school.nz", 
    "@my.bdsc.school.nz", 
    "@outlook.com", 
    "@outlook.co.nz",
    "@yahoo.com", 
    "@yahoo.co.nz"
)

# Declaring global variables 
# Global variable - food_menu_items
# **Dictionary format is inconsistent due to formatting on easygui.multchoicebox() - no other option**
food_menu_items = {
    "Morning Tea                                                     " :  0,
    "   Eggs Benedict Deluxe  + grain toast, hollandaise                         - $13.50"       : 13.50,
    "   Omelette                                                                                            - $12.20"        : 12.20,
    "   Scrambled Eggs + Grain Toast                                                        - $10.00"        : 10.00,
    "   Poached Eggs + Grain Toast                                                           -  $9.90"        :  9.90,
    "   French Toast + Butter + Maple                                                       -  $9.60"        :  9.60,
    "     + berries, whipped cream                                                                      -  +$2.00" :  2.00,
    "   Buttermilk Pancakes                                                                         - $13.50"        : 13.50,
    "     + berries, choc ice cream                                                                      -  +$2.00" :  2.00,
    "   Nutella Pancakes                                                                               - $12.80"        : 12.80,
    "   Double Choc Pancakes                                                                     - $12.00"        : 12.00,
    "   Cheesy Garlic Bread                                                                           -  $4.00"        :  4.00,
    "   Cheese Toastie                                                                                   -  $3.90"        :  3.90,
    "   Mushroom Toastie                                                                            -  $3.90"        :  3.90,
    "   Smashed Avocado Toast                                                                  -  $3.90"        :  3.90,
    "                                         "                                             :  0,
    "Lunch                                    "                                             :  0,
    "   Avocado + Chicken Burger                                                              - $10.20" : 10.20,
    "   Vege Pea Protein Burger                                                                   -  $9.70" :  9.70,
    "   English Muffin Cheese Melt                                                             -  $6.10" :  6.10,
    "   Creamy Chicken Alfredo                                                                  - $13.60" : 13.60,
    "   Meatballs Marinara                                                                            - $13.20" : 13.20,
    "   Pesto Pasta                                                                                          - $12.90" : 12.90,
    "     + GF pasta                                                                                                 -  +$1.30":  1.30,
    "   Mac N' Cheese                                                                                    -  $9.90" :  9.90,
    "   Chicken Nuggets + Fries Combo                                                     - $10.50" : 10.50,
    "   Soy Bao Bun                                                                                        -  $4.50" :  4.50,
    "   Chicken Bao Bun                                                                                -  $4.50" :  4.50,
    "   Butter Chicken + Rice                                                                        - $11.20" : 11.20,
    "   Lamb Dumplings                                                                                -  $9.50" :  9.50,
    "   Wontons                                                                                              -  $8.50" :  8.50,
    "   Grilled Chicken + Hummus                                                              - $11.50" : 11.50,
    "   Tacos                                                                                                    -  $6.10" :  6.10,
    "   Rice Paper Vege Rolls + Sweet Chilli                                                -  $8.50" :  8.50,
    "                                         "                                             :  0,
    "Snacks                                   "                                             :  0,
    "   Salted Chips                                                                                        - $2.50" :  2.50,
    "   Doritos                                                                                                 - $2.50" :  2.50,
    "   Vege Chips                                                                                          - $2.50"  :  2.50,
    "   Chunky Chocolate Chip Cookie                                                      - $4.20"  :  4.20,
    "   Double Choc Muffin                                                                          - $3.90"  :  3.90,
    "   Yoghurt + Fresh Fruit Cup                                                                - $4.50"  :  4.50,
    "   Rice Crackers                                                                                       - $2.20"   :  2.20,
    "   Hot Wedges                                                                                        - $4.50"  :  4.50,
    "   Loaded Fries                                                                                        - $6.50" :  6.50,
    "   Hashbrown                                                                                          - $1.50"  : 1.50,
    "                                         "                                             :  0,
}

drinks_menu_items = {
    "Cold Drinks                       " :  0,
    "   Mango Smoothie                                                                                                  - $6.20" :  6.20,
    "   Mixed Berry Smoothie                                                                                          - $6.20" :  6.20,
    "   Lime Tropical Smoothie                                                                                       - $6.20" :  6.20,
    "   Apple Juice                                                                                                             - $3.60" :  3.60,
    "   Orange Juice                                                                                                          - $3.60" :  3.60,
    "   Mango + Orange Juice                                                                                         - $3.60" :  3.60,
    "   Tropical Juice                                                                                                         - $3.60" :  3.60,
    "   Aloe Vera                                                                                                                - $4.20" :  4.20,
    "   Iced Coffee                                                                                                             - $5.50" :  5.50,
    "   Iced Chocolate                                                                                                       - $4.90" :  4.90,
    "                                  " :  0,
    "Hot Drinks                        " :  0,
    "   Chai Latte                                                                                                                 - $5.20" :  5.20,
    "   Matcha Latte                                                                                                            - $6.10" :  6.10,
    "   Cappuccino                                                                                                              - $7.20" :  7.20,
    "   Espresso                                                                                                                    - $7.50" :  7.50,
    "   Flat White                                                                                                                  - $6.30" :  6.30,
    "   Americano                                                                                                                - $6.80" :  6.80,
    "   Mocha                                                                                                                       - $6.40" :  6.40,
    "   Hot Chocolate                                                                                                          - $4.70" :  4.70,
    "     + deluxe (4 pumps molten choc)                                                                                -  +$1.50":  1.50,
    "     + standard (2 pumps molten choc)                                                                            -  +$0.50":  0.50,
    "   Tea                                                                                                                             - $3.30" :  3.30,
    "                                             " :  0,
    }
order = {}     # empty dictionary to store user's order details

# Declaring All Functions
# Menu Function
# Food Menu Function
def food_order_menu(): 
    food_message = "Please select your food order items."
    title4 = "BDSC School Cafe - All Day Food Menu"
    chosen = easygui.multchoicebox(food_message, title4, list(food_menu_items.keys()))
    if chosen:
        for item in chosen:
            order[item] = food_menu_items[item]

# Drinks Menu Function 
def drinks_order_menu():
    drinks_message = "Please select your drinks order items."
    title8 = "BDSC School Cafe - All Day Food Menu"
    chosen = easygui.multchoicebox(drinks_message, title8, list(drinks_menu_items.keys()))
    if chosen:
        for item in chosen:
            order[item] = drinks_menu_items[item]

# Order Invoice Function 
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
        order_list += f"{item}\n"


    order_invoice = ("===================================================================\n"
                     "                           Order Invoice                           \n"
                     "===================================================================\n"
                     f"Name :                                       {name}\n"
                     f"Occ. :                                       {specify}\n"
                     f"Year :                                       {yr_lvl}\n"
                     f"Email:                                       {user_email}\n"
                     f"Time :                                       {time}\n"
                     "-------------------------------------------------------------------\n"
                     f"Order:\n{order_list}"
                     "-------------------------------------------------------------------\n"
                     f"Subtotal Price:                                         $ {calculate_subtotal_price():.2f}\n"
                     f"GST (15%):                                   						     $ {calculate_subtotal_price() * 0.15:.2f}\n"
                     f"Total Price:                                						      $ {calculate_total_price():.2f}\n"
                     )
    easygui.msgbox(f"Please see your Order Invoice below:\n{order_invoice}", "Invoice Receipt")

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
    easygui.msgbox("Okay. Lets continue onto the login page!")

elif reply == choices[1]:
    # If "No. Exit out of platform." is chosen:
    sys.exit(easygui.msgbox("Goodbye! Come back soon to use BDSC School Cafe Click and Collect!"))

else:
    # If user closes or cancels the dialog box by accident:
    sys.exit(easygui.msgbox("Oh no! You cancelled or closed the dialog box.\nPlease restart BDSC School Cafe Click and Collect platform."))

# Asking user details
# Asking first name details
while True:
    first_name = easygui.enterbox("Enter your first name: ")    # using enterbox so user can enter their name
     # If user closes or cancels the dialog box by accident
    if first_name is None:      # None means nothing was entered
        sys.exit(easygui.msgbox("Oh no! You cancelled or closed the dialog box.\nPlease restart BDSC School Cafe Click and Collect platform."))
    # If user enters valid first name
    elif first_name.isalpha():    # using isalpha() to check if name only contains letters
        first_name = first_name.capitalize()
        break      # breaks loop
    # If user enters any special characters or numbers in first name
    else:
        easygui.msgbox("Invalid input. Please enter only letters for your name.")

# Asking last name details
while True:
    last_name = easygui.enterbox("Enter your last name: ")    # using enterbox so user can enter their name
    
    # If user closes or cancels the dialog box by accident
    if last_name is None:      # None means nothing was entered
        sys.exit(easygui.msgbox("Oh no! You cancelled or closed the dialog box.\nPlease restart BDSC School Cafe Click and Collect platform."))
    
    # If user enters valid last name
    elif last_name.isalpha():    # using isalpha() to check if name only contains letters
        last_name = last_name.capitalize()
        name = f"{first_name} {last_name}"        # assigning 'name' variable combining 'first_name' and 'last_name' variables content
        easygui.msgbox(f"Hi {name}! Please continue filling out user details.")   # greeting user by their name
        break      # breaks loop
    
    # If user enters any special characters or numbers in first name
    else:
        easygui.msgbox("Invalid input. Please enter only letters for your name.")

# Asking if user is student or teaching staff
ask_occupation = "Before we continue further, are you a student or a part of teaching staff?\nPlease specify by choosing one of the options below."
title6 = "Asking Occupation"
occupation_choices = ["Student", "Teaching Staff"]
specify = easygui.choicebox(ask_occupation, title6, occupation_choices)

# Student - Occupation
if specify == occupation_choices[0]:
    # Asking year level details using while loop
    while True:
        yr_lvl = easygui.integerbox("Enter your year level: ")   # using integerbox so integers are only allowed, increased validity
        
        # If user closes or cancels the dialog box by accident
        if yr_lvl is None:      # None means nothing was entered
            sys.exit(easygui.msgbox("Oh no! You cancelled or closed the dialog box.\nPlease restart BDSC School Cafe Click and Collect platform."))

        # If user's year level is within range
        elif yr_lvl in YR_LVL:   # using 'in' to check if year level is within the range of 9-13
            easygui.msgbox(f"Thank you {name} for entering your user details and specifying your current occupation. Your request in using the BDSC School Cafe Click and Collect is approved!")   # confirming user's year level
            break   # breaks loop if a valid year level is entered

        # If user's year level is NOT within range
        else:
            sys.exit(easygui.msgbox(f"Sorry {first_name}, you are not eligible to use the BDSC Cafe Click and Collect.\nSadly, you do not fit the year level range (9-13) requirements."))  # exceeds boundaries of year level range

# Teaching Staff - Occupation
elif specify == occupation_choices[1]:
    # Asking age details using while loop 
    while True:
        age = easygui.integerbox("Enter your age: ")   # using integerbox so integers are only allowed, increased validity
        
        # If user closes or cancels the dialog box by accident
        if age is None:       # None means nothing was entered
            sys.exit(easygui.msgbox("Oh no! You cancelled or closed the dialog box.\nPlease restart BDSC School Cafe Click and Collect platform."))
        
        # If user's age is within range
        elif age in AGE:
            easygui.msgbox(f"Age is within the range. Please continue on to the next part.")
            break   # exits loop once valid age is confirmed
        
        # If user's age is NOT within range
        else:
            sys.exit(easygui.msgbox(f"Sorry {first_name}, you are not eligible to use the BDSC Cafe Click and Collect.\nSadly, you do not meet the age requirements (21-70) for the teaching staff.\n\nIf you think this is a mistake please email:        cafe@bdsc.school.nz"))  # exceeds boundaries of year level range

    # Asking job role details using loop until valid selection
    while True:
        asking_jobrole = "Please select your current, main job role for further verification:"
        title7 = "Job Occupation"
        jobrole_choices = ["", "1. Student Services", "2. Senior Leadership Team", "3. International", "4. Head of Learning Area", "5. Whanau Leader", "6. Teaching Staff", "7. Operational Staff"]

        job = easygui.choicebox(asking_jobrole, title7, jobrole_choices)
        
        # If user closes or cancels the dialog box by accident
        if job is None:         # None means nothing was entered
            sys.exit(easygui.msgbox("Oh no! You cancelled or closed the dialog box.\nPlease restart BDSC School Cafe Click and Collect platform."))
        
        # If user selected the blank option, meaning no valid role chosen
        elif job == "":
            easygui.msgbox(f"Sorry {first_name}, that is not a valid job field. Please specify through options 1. to 7.")
        
        # If user selected a valid job role, approve their access
        else:
            easygui.msgbox(f"Thank you {name} for entering your user details and specifying your current occupation. Your request in using the BDSC School Cafe Click and Collect is approved!")
            yr_lvl = "Teaching Staff"  # Set yr_lvl for teaching staff for invoice purposes (no other way)
            break
        
# If user closes or cancels the dialog box by accident:
else:
    sys.exit(easygui.msgbox("Oh no! You cancelled or closed the dialog box.\nPlease restart BDSC School Cafe Click and Collect platform."))

while True:
    email_prompt = f"Please enter your email address, {first_name}, so we can notify you when your order is ready or if any problems occur:"
    title10 = "Contact: Email Address"

    user_email = easygui.enterbox(email_prompt, title10)

    # If user closes or cancels the dialog box by accident:
    if user_email is None:
        sys.exit(easygui.msgbox("Oh no! You cancelled or closed the dialog box.\nPlease restart BDSC School Cafe Click and Collect platform."))
    
    # If user had valid email     # makes sure email removes whitespace, all lowercase and uses correct, valid email domains
    valid_user_email = user_email.lower().strip()
    if valid_user_email.endswith(ALLOWED_EMAIL_DOMAINS):
        easygui.msgbox(f"Congratulations {first_name}! You have successfully verified your user identity.\nYour email {valid_user_email} contains an approved domain.")
        break
    
    # If user writes invalid syntax in email
    else:
        easygui.msgbox("Invalid syntax. Please try again with maybe a different email address that is valid to these domains below: \n@gmail.com\n@bdsc.school.nz\n@my.bdsc.school.nz\n@outlook.com\n@outlook.nz\n@yahoo.com\n@yahoo.co.nz")

# Asking user what time they would like to pick up their order
while True:
    pickup_time = "What time would you like to pick up your order?"
    title5 = "Order Pickup Time"
    time_choices = ["", "1. Before School", "2. Morning Tea", "3. Lunch", "4. After School"]
    time = easygui.choicebox(pickup_time, title5, time_choices)

    # If user closes or cancels the dialog box by accident:
    if time is None:
        sys.exit(easygui.msgbox("Oh no! You cancelled or closed the dialog box.\nPlease restart BDSC School Cafe Click and Collect platform."))

    # If user selected the blank option, meaning no valid time for order pick up was chosen
    elif time == "":
        easygui.msgbox(f"Sorry {first_name}, that is not a valid order pickup time field.\nPlease specify through options 1. to 4.")

    # If user picks a time for order pickup
    else:
        easygui.msgbox(f"Thank you {first_name} for clarifying when you will be able to pick up your order.")
        break          # breaks while loop and stops code from repeating continuously after user specifies order pickup time

# Order Main Menu
def display_main_menu():
    order.clear()

    def ask_more_items():
        asking_again = "Would you like to order more from the BDSC Cafe Click and Collect?"
        title9 = "Order Main Menu"
        asking_choices_again = ["Yes please! I would like to order more food.", "Yes please! I would like to order more drinks.", "No thanks!"]
        reply2 = easygui.choicebox(asking_again, title9, asking_choices_again)
        if reply2 is None:
            sys.exit(easygui.msgbox("Oh no! You cancelled or closed the dialog box.\nPlease restart BDSC School Cafe Click and Collect platform."))
        return reply2

    while True:
        main_menu = "Would you like to order from the cafe menu? If so, please specify which menu you would like to order from.\nFood or Drinks?"
        title3 = "Order Main Menu"
        choices = ["Take me to the food menu!", "Take me to the drinks menu!", "None, Exit me out of the platform!"]
        reply = easygui.choicebox(main_menu, title3, choices)    # using choicebox to ask user if they want to see the cafe menu or exit

        if reply == choices[0]:
            food_order_menu()
            reply2 = ask_more_items()
            if reply2 == "Yes please! I would like to order more food.":
                food_order_menu()
                easygui.msgbox(f"Sorry {first_name}, you cannot add items to your order more than twice due to other incoming customer orders.\nTo place more orders, exit application and login again.\nPlease continue on to the next page to view your invoice.")
                invoice()
                easygui.msgbox(f"Thank you for your patience. Your order has been confirmed.\nHave a great day {first_name} and please come back soon to the BDSC Cafe Click and Collect Program!", "BDSC Cafe Click and Collect")
                break

            elif reply2 == "Yes please! I would like to order more drinks.":
                drinks_order_menu()
                easygui.msgbox(f"Sorry {first_name}, you cannot add items to your order more than twice due to other incoming customer orders.\nTo place more orders, exit application and login again.\nPlease continue on to the next page to view your invoice.")
                invoice()
                easygui.msgbox(f"Thank you for your patience. Your order has been confirmed.\nHave a great day {first_name} and please come back soon to the BDSC Cafe Click and Collect Program!", "BDSC Cafe Click and Collect")
                break
            else:
                easygui.msgbox(f"Thank you for ordering {first_name}!")
                invoice()
                easygui.msgbox(f"Thank you for your patience. Your order has been confirmed.\nHave a great day {first_name} and please come back soon to the BDSC Cafe Click and Collect Program!", "BDSC Cafe Click and Collect")
                break

        elif reply == choices[1]:
            drinks_order_menu()
            reply2 = ask_more_items()
            if reply2 == "Yes please! I would like to order more food.":
                food_order_menu()
                easygui.msgbox(f"Sorry {first_name}, you cannot add items to your order more than twice due to other incoming customer orders.\nTo place more orders, exit application and login again.\nPlease continue on to the next page to view your invoice.")
                invoice()
                easygui.msgbox(f"Thank you for your patience. Your order has been confirmed.\nHave a great day {first_name} and please come back soon to the BDSC Cafe Click and Collect Program!", "BDSC Cafe Click and Collect")
                break
            elif reply2 == "Yes please! I would like to order more drinks.":
                drinks_order_menu()
                easygui.msgbox(f"Sorry {first_name}, you cannot add items to your order more than twice due to other incoming customer orders.\nTo place more orders, exit application and login again.\nPlease continue on to the next page to view your invoice.")
                invoice()
                easygui.msgbox(f"Thank you for your patience. Your order has been confirmed.\nHave a great day {first_name} and please come back soon to the BDSC Cafe Click and Collect Program!", "BDSC Cafe Click and Collect")
                break
            else:
                easygui.msgbox(f"Thank you for ordering {first_name}!")
                invoice()
                easygui.msgbox(f"Thank you for your patience. Your order has been confirmed.\nHave a great day {first_name} and please come back soon to the BDSC Cafe Click and Collect Program!", "BDSC Cafe Click and Collect")
                break

        elif reply == choices[2]:
            sys.exit(easygui.msgbox(f"Thank you for using BDSC Cafe Click and Collect! We hope you come back soon {first_name}!"))
            break
        else:
            sys.exit(easygui.msgbox("Oh no! You cancelled or closed the dialog box.\nPlease restart BDSC School Cafe Click and Collect platform."))
            break

display_main_menu()