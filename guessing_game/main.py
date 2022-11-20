import random
from art import logo
# Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

EASY_LEVEL = 10
HARD_LEVEL = 5

def check_answer(guessed_num, answer, turns):    
    """checks answer against guess. Returns the number of turns remaining."""
    if guessed_num < answer:
        print("Too low!")
        return turns - 1 
    elif guessed_num > answer:
        print("Too high!")
        return turns - 1
    else:
        print("You've guessed the right number. You win!")

def level():
    """Determine difficulty level"""
    difficulty = input("Chose a difficulty level: Type 'e' for easy or 'h' for hard: ").lower()
    if difficulty == "e":
        return EASY_LEVEL
    elif difficulty == "h":
        return HARD_LEVEL
    else:
        print("Invalid selection")

def game():
    """Functioono to run the game"""
    print(logo)
    print("Welcome to my Number Guessing Game!")

    print("I’m thinking of a number between 1 and 100. Tell me what it is")

    answer = random.randint(1, 100)
    print(f" psst.. the answer is {answer}")

    turns = level()
    guessed_num = 0

    #Repeat the guessing functionality if they get it wrong.
    while guessed_num != answer:
        print(f"You have {turns} attempts remaining to guess the number")
        
        guessed_num = int(input("Make a guess: "))
        
        turns = check_answer(guessed_num, answer, turns)

        #Track the number of turns and reduce by 1 if they get it wrong.
        if turns == 0:
            print("You have no attempts remaining. You lose!")
            return 
        #elif guessed_num != answer:
            print("Guess again")

game()

        
