# Word-Guessing-Game
The game is based on Python and takes an input file containing 4030 4-letter English words.

## Description

In this word guessing game, user will be given a randomly generated 4-letter word from a user provided file. The player must then continue to guess the whole word or a letter at a time until the player guesses the correct word or gives up. Player can quit at any time. Each letter in the English language is used with a certain frequency (“e” is the most common letter, “z” the least). On quitting the game, the score from each round will be displayed, along with the original word, the status of the game (correct guess or not), the number of guesses required, and the final score for that game.

## Rules

* The letters that are still blank at the time of a correct guess will be summed together to give a total.
* The number of letters that the player turns over also affects the score. The sum is divided by the number of times the player requests a letter.
* An incorrect guess costs 10% of the score for the current word.
* When the player gives up, the points lost are the sum of the uncovered letters.

**Python-style documentation is provided for the system and pydoc can be used to generate full web-based API for the application.**


