############### Blackjack Project #####################

############### Our Blackjack House Rules #####################

# The deck is unlimited in size.
# There are no jokers.
# The Jack/Queen/King all count as 10.
# The the Ace can count as 11 or 1.
# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.
# The computer is the dealer.
# Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

import random
from os import system, name
import sys
from art import logo
# import sleep to show output for some time period
from time import sleep


def clear():
    """Clear conosole before restarting another game."""
    # for wndowes os
    if name == 'nt':
        _ = system('cls')
    # for Mac NS Linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def deal_card():
    """Returns random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    """Function takes a list of cards, checks for blackjack,if score > 21 or return a score"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
        sum(cards)
    return sum(cards)


def compare(user_score, computer_score):
    """Compare score and determine who won"""
    if user_score > 21 and computer_score > 21:
        return "You went over. You lose 😤"

    if user_score == computer_score:
        return "It's a DRAW 🙃"
    elif computer_score == 0:
        return "You LOSE! Your opponent has Blackjack 😱"
    elif user_score == 0:
        return "You WIN with a Blackjack 😎"
    elif user_score > 21:
        return "You went over. You LOSE 😭"
    elif computer_score > 21:
        return "Your opponent went over. You WIN 😁"
    elif user_score > computer_score:
        return "You WIN 😃"
    else:
        return "You LOSE 😤"


def play_game():
    """Let user play game until they chose to stop"""
    print(logo)
    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        # Calling function calculate_score()
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards are: {user_cards} and your score is {user_score}")
        print(f"Computer's first card: {computer_cards[0]} ")

        if computer_score == 0 or user_score == 0 or user_score > 21:
            is_game_over = True
            print("Game over!")
        else:
            new_draw = input(
                "Do you want to draw another cards? Tpye 'yes' or 'no' ")
            if new_draw == "yes":
                user_cards.append(deal_card())
            else:
                is_game_over = True
                print(f" Your score is: {user_score}")

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    compare(user_score, computer_score)

    print(f"Your cards are: {user_cards} and final score is {user_score}")
    print(
        f"Your opponent cards are: {computer_cards} for a final score of {computer_score}")
    print(compare(user_score, computer_score))

    while input("Do you want to play another game? Tpye 'yes' or 'no': ") == "yes":
        clear()
        play_game()


play_game()
