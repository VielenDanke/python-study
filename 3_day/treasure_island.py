print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

unknown_direction_error_message = "Unknown direction. Game over"

direction = input("You are at a crossroad. What direction you want to go? Type 'left' or 'right'")

if direction == "left":
    print("You are in good direction. Suddenly you meet a Wanderer. Road is close. Swim or go to the bridge")
    direction = input("What will you choose? Do you trust a Wanderer? Type 'swim' or 'bridge'")
    if direction == "swim":
        print("Sharks eat well. Thanks. Game over")
    elif direction == "bridge":
        direction = input(
            "Your road is going well. Suddenly you see the cross and shovel. What will you do? Type 'walking' or "
            "'dig'")
        if direction == "walking":
            print("Sorry. Treasure was so closed. But you didn't find it. Game over")
        elif direction == "dig":
            print("Great choice. You found a treasure. Congratulation. You won this game")
        else:
            print(unknown_direction_error_message)
    else:
        print(unknown_direction_error_message)
elif direction == "right":
    print()
else:
    print(unknown_direction_error_message)
