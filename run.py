import random


def deal_card():
    """
    Returns a random card from the deck
    """
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

# Deal the user and computer 2 cards each using the deal_card()
user_card = []
computer_card = []