import art

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculator():
    """ Calculator """
    print(art.logo)
    should_continue = True
    num1 = float(input("Enter the first number: "))

    while should_continue:
        for symbol in operations:
            print(symbol)
        operation_symbol = input("Pick an operation from the line above: ")
        num2 = float(input("Enter the second number: "))

        calculation_function = operations[operation_symbol]
        result = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {result}")

        if input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ") == "y":
            num1 = result
        else:
            should_continue = False
            print("\n\n")
            calculator()

calculator()
