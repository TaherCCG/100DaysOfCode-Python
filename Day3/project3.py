# Techville text based game

print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|___________________|__________________|_____________________|_______
|                   |                           |                     |       |
|___________________|___________________________|_____________________|_______|
          |                   |                  |                     |
 _________|__________█████____|____█████_________|_____________________|_______
|                   |███  ██ |  ███  ██         |  █████              |       |
|___________________|███████ |████████          |  ███████            |_______|
          |          |███  ██ | ███  ██          |  █████              |
 _________|__________|███  ██ | ███████          |  █████              |_______
|                   |███████ | ███  ██          |█████████           |       |
|___________________|███  ██ | ███  ██          | ███████             |_______|
          |          |███  ██ | ███████         |  █████              |
 _________|__________|███  ██ | ███  ██         |  █████              |_______
|                   |███████ | ███████         | ████████           |       |
|___________________|███  ██ | ███  ██         |█████████           |_______|
          |          |███  ██ | ███████        |  ████████          |
 _________|__________|███  ██ | ███████        |  ████████         |_______
|                   |███████ | ███████        |  █████████        |       |
|___________________|███████ | ███████        |██████████        |_______|
          |                   |                  |                     |
*******************************************************************************
''')

print("Welcome to the vibrant city of Techville.")
print("Your mission is to uncover the hidden tech vault.")


# First decision
print("You find yourself in the bustling city of Techville, standing at a fork in the road.")
decision1 = input("Do you go left towards the neon-lit street or right towards the alleyway? ").lower()
if decision1 == "left":
    # Second decision
    print("You come across a sleek electric scooter parked by the roadside.")
    decision2 = input("Do you ride the scooter or wait for an autonomous taxi? Type 'ride' or 'wait': ").lower()
    if decision2 == "wait":
        # Third decision
        print("The taxi arrives and takes you to a futuristic building with three smart doors.")
        decision3 = input("Which door do you choose? Red, Blue, or Yellow? ").lower()
        if decision3 == "yellow":
            print("Congratulations! You've found the hidden tech vault. You Win!")
        elif decision3 == "red":
            print("Oh no! You've entered a restricted area and the alarm goes off. Game Over.")
        elif decision3 == "blue":
            print("Yikes! You've walked into a room full of malfunctioning robots. Game Over.")
        else:
            print("Invalid choice. Game Over.")
    else:
        print("You accidentally crash the scooter into a drone delivery station. Game Over.")
else:
    print("You stumble into a shadowy alley and fall into an underground bunker. Game Over.")
