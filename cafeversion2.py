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
    easygui.msgbox("Okay. Lets continue on to ordering!")

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