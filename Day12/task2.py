# Accessible anywhere
my_global_var = 1

def my_function():
    # Only accessible within my_function()
    my_local_var = 2


for _ in range(10):
    # Accessible anywhere
    my_block_var = 3


game_level = 3
enemies = ["Squid", "Goblin", "Spider"]

def create_enemy():
    new_enemy = ""
    if game_level < 5:
        new_enemy = enemies[0]

    print(new_enemy)


# The scope of a variable is the region of the code where it's defined.
# The scope of a variable determines where it can be accessed from.