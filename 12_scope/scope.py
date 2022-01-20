enemies = 1


# Modifying global scope
def increase_enemies():
    # allows modifying global variables
    global enemies
    enemies += 1
    print(f"Inner scope: {enemies}")


# better return as the output then using global
def increase_enemies_better():
    print(f"Inner scope: {enemies}")
    return enemies + 1


increase_enemies()
enemies += increase_enemies_better()
print(f"Outer scope: {enemies}")

# ****************************************************************************

# Local scope (Variable inside the function)
# Cannot see the variable which is inside the function from outside the function

# Global scope (Variable at the top level of the file, not within another function)
# See in all the methods and blocks

# Global constants
# Naming all upper case and separated by _
PI = 3.14159

# No block scope (excluded functions - cannot access from inside the function)
game_level = 3
enemies = ["Skeleton", "Zombie", "Alien"]

if game_level < 5:
    new_enemy = enemies[0]

print(new_enemy)
