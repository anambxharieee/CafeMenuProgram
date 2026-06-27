'''This text-based program is made for the school cafe. 
The school cafe wants a menu-driven program for a 
cafe order click and collect app to be created. 
The program is meant to display a list of products 
and prices, allow users to login and place orders 
and then provide an order invoice relevant details.'''

# Modules
import sys # import sys module so sys functions can be used in program

# Declaring constants
YR_LVL = range(9, 14)
AGE = range(13, 19)

# This is the main menu of the cafe order click and collect app
print("Welcome to the School Cafe Click and Collect!") # User welcome message
login = input("Do you want to login? (yes/no): ")      # Login prompt (yes or no)
if login.lower() == "no":
    sys.exit(print("Thank you for visiting School Cafe Click and Collect! Come back soon!"))

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
            age = int(input("Enter your age: "))         # Age input prompt
            if int(age) in AGE:
                print("Age is valid.")
                break
            else:
                sys.exit("Sorry this app is only for students aged between 13 and 18.")
        except ValueError:
            print("Invalid input. Please enter a numeric age.")
    
    while True:
        try:
            yr_level = int(input("Enter your year level: "))    # year level input prompt
            if yr_level in YR_LVL:
                print("Login successful!")
                break
            else:
                sys.exit("Sorry, you are not eligible to use this app.")
        except ValueError:
            print("Invalid input. Please enter only numeric values.")

   # Displaying All Day Menu 
    print("-----All Day Menu------")
    print("Eggs Eggs Eggs - feat. white/grain toast                 \n"
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

    order = []

    # Asking user for their order and if they want to order anything else
    items = input("What would you like to order today? ")
    order.append(items)
    anything_else = input("Would you like to order anything else? (yes/no): ")

    while True:         # while loop to allow user to order multiple producrts without having to restart the program
        if anything_else.lower() == "yes":
            items = input("What else would you like to order? ")
            order.append(items)
            anything_else = input("Would you like to order anything else? (yes/no): ")     # making sure user is finished ordering before breaking loop
        else:
            break           # breaks loop after user is finished ordering

    # Displaying order summary + invoice details
    print("-----Order Summary-----")
    print(f"Customer Name: {user_name}\nAge: {age}\nYear Level: {yr_level}\nItems Ordered: {order}")