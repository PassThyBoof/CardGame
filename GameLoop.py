import random


player1 = ""
player2 = ""
card_deck = [
    ["red", 1], ["red", 2], ["red", 3], ["red", 4], ["red", 5],
    ["red", 6], ["red", 7], ["red", 8], ["red", 9], ["red", 10],
    ["yellow", 1], ["yellow", 2], ["yellow", 3], ["yellow", 4], ["yellow", 5],
    ["yellow", 6], ["yellow", 7], ["yellow", 8], ["yellow", 9], ["yellow", 10],
    ["black", 1], ["black", 2], ["black", 3], ["black", 4], ["black", 5],
    ["black", 6], ["black", 7], ["black", 8], ["black", 9], ["black", 10],
]


def card_colour_winner(card1, card2):
    if card1 == "red" and card2 == "black":
        winning_card = "red"
    elif card1 == "yellow" and card2 == "red":
        winning_card = "yellow"
    elif card1 == "black" and card2 == "yellow":
        winning_card = "black"
    else:
        winning_card = "error"
    return winning_card


def card_digit_winner(card1, card2):
    if card1 > card2:
        winning_card = card1
    if card2 > card1:
        winning_card = card2
    return winning_card


def main_game_loop():
    deck = random.sample(card_deck, 30)
    for game_round in range(len(shuffled_deck)):
        deck_size = len(shuffled_deck)
        player_one_card = shuffled_deck.pop(deck_size - 1)
        player_two_card = shuffled_deck.pop(deck_size - 2)
        if player_one_card[0] == player_two_card[0]:
            winner = card_colour_winner(player_one_card, player_two_card)
        else:
            winner = card_digit_winner(player_one_card, player_two_card)
        print("Player1's card is [{0}] and Player2's card is [{1}]".format(player_one_card, player_two_card))
        print("The winner of round{0} is {1}".format(game_round, winner))
        print("leftover deck is :", deck)

main_game_loop()