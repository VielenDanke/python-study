import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
blackjack_lucky_number = 21
lower_border = 17
upper_border = 21


def card_deal(player_hand):
    next_number = random.choice(cards)
    if next_number == 11:
        if next_number + player_hand > 21:
            next_number = 1
        else:
            next_number = 11
    return next_number


def game():
    start_score = 0

    dealer_hand = card_deal(start_score) + card_deal(start_score)

    print(f"Dealer hand: {dealer_hand}")

    player_hand = card_deal(start_score) + card_deal(start_score)

    if player_hand == blackjack_lucky_number:
        print("Blackjack!")
        return

    while player_hand < blackjack_lucky_number:
        print(f"Player hand: {player_hand}")

        player_answer = input("Hit? Type 'y' or 'n'").lower()

        if player_answer == "y":
            player_hand += card_deal(player_hand)
        else:
            break

    if player_hand > 21:
        print(f"Player took too much {player_hand}. Dealer wins!")
        return

    while dealer_hand <= blackjack_lucky_number:
        if lower_border <= dealer_hand <= upper_border:
            break
        else:
            dealer_hand += card_deal(player_hand)

    final_message = f"Player result: {player_hand}. Dealer result: {dealer_hand}"

    if dealer_hand > 21:
        print(f"Player wins! {final_message}")
    elif dealer_hand < player_hand:
        print(f"Player wins! {final_message}")
    elif dealer_hand == player_hand:
        print(f"Draw! {final_message}")
    else:
        print(f"Dealer wins! {final_message}")


game()
