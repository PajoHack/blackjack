import random
from art import logo
import os

def clear():
    # for Windows
    if os.name == 'nt':
        _ = os.system('cls')
    # for Unix (Linux, macOS)
    else:
        _ = os.system('clear')


def deal_card():
    """
    Returns a random card from the deck.
    
    The deck consists of 4 suits with cards 2-10, Jack, Queen, King (all valued at 10), and Ace (valued at 11 or 1).
    This function simulates drawing a single card from a deck and returns its value.
    """
    # Define a list of card values. Note: 11 represents Ace, while 10 appears four times to represent 10, Jack, Queen, and King.
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    # Randomly select a card from the list and return it.
    card = random.choice(cards)
    return card


def calculate_score(cards):
    """
    Calculates the score of a hand of cards.

    Args:
        cards (list): A list of integers where each integer represents the value of a card in the hand.
    
    Returns:
        int: The total score calculated from the cards. If the hand is a blackjack (an Ace and a 10-value card),
        returns 0. Adjusts the value of Ace from 11 to 1 if the total score exceeds 21 to prevent busting.
    """
    # Check for a blackjack (Ace and 10) and return 0 (indicating a special win condition).
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    
    # If there's an Ace (value 11) and the score exceeds 21, replace the Ace with a 1 (by removing an 11 and adding a 1).
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    
    # Return the sum of the cards in the hand as the total score.
    return sum(cards)

def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "You loose, Dealer has Blackjack"
    elif user_score == 0:
        return "*** You win with a Blackjack !!! ***"
    elif user_score > 21:
        return "Bust! you went over 21"
    elif computer_score > 21:
        return "Dealer is bust! You win!"
    elif user_score > computer_score:
        return "You win"
    else:
        return "You lose"


def get_user_input(prompt):
    """
    Validates user input, ensuring it's either 'y' or 'n'.
    """
    while True:
        user_input = input(prompt).lower()
        if user_input in ['y', 'n']:
            return user_input
    else:
        print("Invalid input. Please type 'y' for yes or 'n' for no.")


def play_game():
    print(logo)
    # Initialize lists to hold the user's and computer's cards.
    user_cards = []
    computer_cards = []
    is_game_over = False


    # Deal two cards each to the user and the computer.
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        # Calculate the scores of the user and the computer based on the initial two cards dealt. 
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}\n")

        # Determine if the game should end immediately based on the initial hands.
        if user_score == 0 or computer_score == 0 or user_score >21:
            # If the user or computer has a Blackjack (score of 0) or the user busts (score > 21), the game ends.
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            print()
            if user_should_deal == "y":
                # If the user decides to take another card, deal one more card to the user's hand.
                user_cards.append(deal_card())
            else:
                # If the user decides not to take another card, the game moves towards conclusion.
                is_game_over = True


    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
        

    print(f"Your final hand: {user_cards}, Final score: {user_score}\n")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}\n")
    print(compare(user_score, computer_score))
    
    
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    clear()
    play_game()