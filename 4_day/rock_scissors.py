import random

seed = int(input("Insert random seed number"))

random.seed(seed)

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_list = [rock, paper, scissors]

player_number = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors"))

computer_number = random.randint(0, len(game_list) - 1)

player_win_message = "Player win"
no_winner_message = "No winner"
computer_win_message = "Computer win"

rules = [[paper, rock, player_win_message], [paper, paper, no_winner_message], [paper, scissors, computer_win_message],
         [rock, paper, computer_win_message], [rock, rock, no_winner_message], [rock, scissors, player_win_message],
         [scissors, rock, computer_win_message], [scissors, paper, player_win_message], [scissors, scissors, no_winner_message]]

player = game_list[player_number]
computer = game_list[computer_number]

print(f"Player:\n {player}")
print(f"Computer:\n {computer}")

win_message = ""

for figure in rules:
    if player == figure[0] and computer == figure[1]:
        win_message = figure[2]

if len(win_message) == 0:
    print("Game error")
print(win_message)
