MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    },
    "black tea": {
        "ingredients": {
            "water": 200,
            "tea": 10,
        },
        "cost": 1.0,
    },
    "green tea": {
        "ingredients": {
            "water": 200,
            "tea": 10,
        },
        "cost": 1.2,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "tea": 50,
}

profit = 0 


def print_report():
    """Print the current resource levels and profit."""
    print("\n\n+-------------------+")
    print("      Resources     ")
    for resource in resources:
        print(f"{resource}: {resources[resource]}")
    print("+-------------------+")
    print(f"Profit: £{profit:.2f}")
    print("+-------------------+\n\n")
    return


def check_resources(order):
    """Check if there are enough resources to make the selected drink."""
    for ingredient in MENU[order]["ingredients"]:
        if resources[ingredient] < MENU[order]["ingredients"][ingredient]:
            print(f"Sorry there is not enough {ingredient}.")
            return False
    return True


def process_coins():
    """Process coins inserted by the user and calculate the total amount."""
    print("Please insert coins.")
    total = int(input("How many Pound Coins? ")) * 1.00
    total += int(input("How many 50p? ")) * 0.50
    total += int(input("How many 10p? ")) * 0.10
    total += int(input("How many pennies? ")) * 0.01
    return total


def check_transaction(order, total):
    """Check if the inserted coins are enough to buy the selected drink."""
    if total < MENU[order]["cost"]:
        print("Sorry that's not enough money. Money refunded.")
        return False
    return True


def make_coffee(order):
    """Deduct the required ingredients from resources and serve the coffee."""
    for ingredient in MENU[order]["ingredients"]:
        resources[ingredient] -= MENU[order]["ingredients"][ingredient]
    print(f"Here is your {order} ☕️. Enjoy!")


def display_menu():
    """Display the menu with available drinks and their prices."""
    print("\n\n")
    print("+------------------------------+")
    print("Welcome to the Coffee Machine!")
    print("Menu:")
    for drink, details in MENU.items():
        print(f"{drink.capitalize()}: £{details['cost']:.2f}")
    print()
    print("+------------------------------+")
    print("Type 'off' to turn off the coffee machine.")

def coffee_machine():
    """Main function to run the coffee machine."""
    global profit
    while True:
        display_menu()
        order = input("What would you like? (espresso/latte/cappuccino/black tea/green tea): ").lower()
        
        if order == "off":
            print("Shutting down the coffee machine...")
            break
        elif order == "report":
            print_report()
        elif order in MENU:
            print(f"The price of {order} is £{MENU[order]['cost']:.2f}")
            if check_resources(order):
                total = process_coins()
                if check_transaction(order, total):
                    change = total - MENU[order]['cost']
                    print("\n\n\nProcessing payment...")
                    print("+-------------------+")
                    print(f"Thank you for your purchase! 🥳")
                    print(f"Here is £{change:.2f} in change.")
                    profit += MENU[order]['cost']
                    print("+-------------------+\n")
                    make_coffee(order)
        else:
            print("Invalid input. Please try again.")


coffee_machine()
