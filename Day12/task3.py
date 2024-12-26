# Modifying Global Scope

enemies = 1


def increase_enemies(enemy):
    # global enemies
    # enemies += 1    # This is trying to modify the global variable directly, but it won't work as there is a scope issue, and this variable is not defined in the local scope.
    print(f"enemies inside function: {enemies}")
    # Instead of modifying the global variable directly, we can return the new value and assign it to the global variable.
    return enemy + 1

enemies = increase_enemies(enemies)
print(f"enemies outside function: {enemies}")