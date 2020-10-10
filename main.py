import UserValidation
import GameLoop


def validate_player1():
    print("************* Validate Player 1 ****************")
    choice = input("Do you want to 'signup' or 'login' :")
    while not (choice == "signup" or choice == "login"):
        choice = input("only choose 'signup' or 'login':")
    if choice == "signup":
        UserValidation.sign_up()
        player = UserValidation.login()
    elif choice == "login":
        for i in range(3):
            player = UserValidation.login()
            if player != False:
                print("********* {0} is logged in as Player1 ********".format(player))
                print("password was incorrect 3 times in a row")
                print("")
                return player
    validate_player1()


def validate_player2():
    print("************* Validate Player 2 ****************")
    choice = input("Do you want to 'signup' or 'login' :")
    while not (choice == "signup" or choice == "login"):
        choice = input("only choose 'signup' or 'login':")
    if choice == "signup":
        UserValidation.sign_up()
        player = UserValidation.login()
    elif choice == "login":
        for i in range(3):
            player = UserValidation.login()
            if player != False:
                print("********* {0} is logged in as Player2 ********".format(player))
                print("password was incorrect 3 times in a row")
                print("")
                return player
    validate_player2()


player1 = validate_player1()
player2 = validate_player2()


def main_game_loop():
    deck = shuffled_deck
    deck_size = len(deck)
    game_round = 0
    while deck_size > 1:
        game_round += 1
        player_one_card = deck[deck_size - 1]
        player_two_card = deck[deck_size - 2]
        print(player_one_card, player_two_card)
        if player_one_card[0] == str and player_two_card[0] == str:
            winner = card_colour_winner(player_one_card, player_two_card)
            print("The winner of round{0}".format(game_round, winner))
        deck_size = deck_size - 2
    print("leftover deck is :", deck)

