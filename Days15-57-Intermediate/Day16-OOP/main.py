# Importing necessary classes from different modules
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Creating instances of MoneyMachine, CoffeeMaker, and Menu classes
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

# Variable to keep the coffee machine running
is_on = True

# Main loop to keep the program running until 'off' is chosen
while is_on:
    # Get available menu items
    options = menu.get_items()
    # Prompt user for their choice
    choice = input(f"What would you like? ({options}): ")
    # Turn off the coffee machine
    if choice == "off":
        is_on = False
    # Print the current report of resources and money
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    # Process the order if a drink is selected
    else:
        drink = menu.find_drink(choice)
        # Check if there are sufficient resources and process payment
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            # Make the coffee if both checks pass
            coffee_maker.make_coffee(drink)
