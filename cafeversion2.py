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
order = {}  # empty dictionary to store user's order details

# Menu Function
def order_menu():
    menu = ("-----All Day Menu-----\n"
            "\n"
            "Eggs Eggs Eggs - feat. white/grain toast                 \n"
            "  -> Eggs Benedict Deluxe                         $17.50 \n"
            "  -> Custom Omelette                              $17.50 \n"
            "  -> Omelette                                     $15.20 \n"
            "  -> Scrambled Eggs                               $15.00 \n"
            "  -> Poached Eggs                                 $12.90 \n"
            "\n"
            "Toast Toast Toast                                        \n"
            "  -> French Toast + Butter                         $9.60 \n"
            "         * berries, banana, maple syrup          + $2.00ea\n"
            "  -> Cheesy Garlic Deluxe                          $4.00 \n"
            "  -> Cheese Toastie                                $3.90 \n"
            "  -> Mushroom Toastie                              $3.90 \n"
            "  -> Smashed Avocado                               $3.90 \n"
            "\n"
            "Pancakes Pancakes Pancakes                                \n"
            "  -> Classic Buttermilk + Maple Syrup              $13.50 \n"
            "         * berries, molten chocolate, ice cream  + $2.00ea\n"
            "  -> Nutella + Chocolate Ice Cream                 $12.80 \n"
            "  -> Butter + Vanilla Ice Cream                    $12.00 \n"
            "\n"
            "Burgers Burgers Burgers                                   \n"
            "  -> Smashed Avocado + Chicken                     $10.20 \n"
            "  -> Vege Patty + Leafy Greens                     $8.70  \n"
            "  -> Hamburger + Cheese Melt                       $8.50  \n"
            "  -> Cheeseburger + English Muffin                 $6.10  \n"
            "\n"
            "Pasta Pasta Pasta                                         \n"
            "        * fettuccine, penne, spagetti, macaroni    $0.00  \n"
            "        * GF pasta                               + $1.30ea\n"
            "  -> alfredo + creamy chicken                      $13.60 \n"
            "  -> marinara + meatballs                          $13.20 \n"
            "  -> pesto                                         $12.90 \n"
            "  -> mac n' cheese                                 $9.90  \n"
            "\n"
            "Drinks Drinks Drinks                                      \n"
            "COLD                                                      \n"
            "  -> Smoothies                                     $6.20  \n"
            "       * mango, mixed berry, lime tropical twist          \n"
            "  -> Juices                                        $3.60  \n"
            "       * apple, orange, mango + orangem, tropical         \n"
            "  -> Aloe Vera                                     $4.20  \n"
            "  -> Iced Coffee                                   $5.50  \n"
            "  -> Iced Chocolate                                $4.90  \n"
            "HOT                                                       \n"
            "  -> Chai Latte                                    $5.20  \n"
            "  -> Matcha Latte                                  $6.10  \n"
            "  -> Cappuccino                                    $7.20  \n"
            "  -> Espresso                                      $7.50  \n"
            "  -> Flat White                                    $6.30  \n"
            "  -> Americano                                     $6.80  \n"
            "  -> Mocha                                         $6.40  \n"
            "  -> Hot Chocolate                                 $5.90  \n"
            "      * DELUXE: 4 pumps of molten chocolate      + $1.50ea\n"
            "      * STANDARD: 2 pumps of molten chocolate    + $0.00ea\n"
            "  -> Tea                                           $3.30  \n"
          )
    easygui.codebox("BDSC School Cafe - All Day Menu", "Cafe Menu", menu)

# Function to calculate total price of order
def calculate_total_price(order):
    return(math.fsum(order.values()))   # using math to carry out math.fsum() so that total price of order can be calculated through addition

# Welcoming user
welcome = "Welcome to BDSC School Cafe Click and Collect!"   # informs user of the name of the app and warmly welcomes the user to it.
title = "Welcome Page"
easygui.msgbox(welcome, title) # printing welcome messagebox to user

# Asking if user wishes to proceed
proceed = "BDSC School Cafe Click and Collect will need you to enter some of your details.\nDo you wish to continue?"
title = "Permission to Ask User Details"
choices = ["Yes. Login into platform", "No. Exit out of platform."]
reply = easygui.choicebox(proceed, title, choices)    # using choicebox to ask user which option they want to choose (login or exit)

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
        title = "Main Menu"
        choices = ["Yes. Show me the menu!", "No. Exit out of platform."]
        reply = easygui.choicebox(main_menu, title, choices)    # using choicebox to ask user if they want to see the cafe menu or exit
        
        if reply == choices[0]:
            order_menu()

        elif reply == choices[1]:
            sys.exit(easygui.msgbox("Sad to see you go! Come back soon!"))
        
        else:
            sys.exit(easygui.msgbox("Oh no! You cancelled or closed the dialog box.\nPlease restart BDSC School Cafe Click and Collect platform."))

display_main_menu()