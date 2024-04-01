Blackjack Game in Python
========================

This Python program simulates a simple game of Blackjack (also known as 21), where the player goes up against a computer dealer. The goal is to get a hand with a value as close to 21 as possible, without going over.

Features
--------

-   The game is played with a simple console interface.
-   A standard deck of cards is simulated, where each card's value is straightforward: numbers 2 through 10 are worth their face value, Jack/Queen/King are each worth 10, and Ace can be worth 1 or 11.
-   The player and the computer (dealer) start with two cards. The player can see one of the dealer's cards.
-   The player can choose to "Hit" to take another card or "Stand" to hold their total.
-   The dealer must hit if their score is below 17.
-   The game supports multiple rounds until the player decides to quit.

How to Run
----------

Ensure you have Python installed on your system. This game uses the `random` module for card drawing, the `art` module for ASCII art (specifically for the Blackjack logo), and `os` module for clearing the console screen.

Clone or download the project to your local machine.

Navigate to the directory containing the game file.
Run the script: `python blackjack_game.py`

Game Instructions
-----------------

-   After starting the game, you will be asked if you want to play a game of Blackjack. Type `'y'` for yes or `'n'` for no.
-   If you choose to play, the game will begin, and you'll be dealt two cards.
-   You'll see your cards and the total score, as well as one of the dealer's cards.
-   Choose whether to "Hit" or "Stand":
    -   Type `'y'` to draw another card.
    -   Type `'n'` to end your turn.
-   After your turn ends, the dealer's turn will proceed automatically according to the rules.
-   The game concludes when both you and the dealer have finished your turns. The winner will be announced based on the scores.
-   You will then be asked if you want to play another round.

Dependencies
------------

-   Python 3.x

Disclaimer
----------

This game is for educational purposes only. It simulates a Blackjack game and does not involve any real gambling.

Enjoy the game, and feel free to contribute to its development!
