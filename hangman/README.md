# Hangman Game

A simple Python command-line Hangman game where the player guesses letters to reveal a hidden word before the hangman is fully drawn.

## Description

The game randomly selects a word from a word list, displays hidden letters as underscores, and allows the player to guess one letter at a time. Incorrect guesses draw parts of the hangman, while correct guesses reveal matching letters in the word.

## Features

* Random word selection from an external word list
* Input validation for single-letter guesses
* Tracks previously guessed letters
* ASCII art hangman display
* Reveals correct letters in the word
* Win and lose conditions
* Playable in the terminal

## Concepts Practiced

* Functions
* Lists
* Sets
* Dictionaries
* Loops
* Conditional statements
* String manipulation
* Input validation
* Module imports
* Random module

## How It Works

1. Choose a random word from `wordList.py`.
2. Create a hidden hint using underscores (`_ _ _`).
3. Display the current hangman stage and hint.
4. Ask the player to enter a letter.
5. Validate the input and check if the letter was already guessed.
6. If the guess is correct, reveal all matching letters.
7. If the guess is incorrect, increase the hangman stage.
8. Repeat until the player wins or loses.

## Example

The word might update to:

## Hangman Stages

| Wrong Guesses | Hangman      |
| ------------- | ------------ |
| 0             | Empty        |
| 1             | Head         |
| 2             | Body         |
| 3             | One arm      |
| 4             | Both arms    |
| 5             | One leg      |
| 6             | Full hangman |

## Project Flow

```text
Start
  ↓
Choose Random Word
  ↓
Create Hidden Hint (_ _ _)
  ↓
Display Hangman & Hint
  ↓
Get User Guess
  ↓
Validate Input
├─ Invalid → Ask Again
└─ Valid
      ↓
Already Guessed?
├─ Yes → Ask Again
└─ No
      ↓
Guess In Word?
├─ Yes → Reveal Letter(s)
└─ No  → Increase Wrong Guess
      ↓
Word Complete?
├─ Yes → Win
└─ No
      ↓
Max Wrong Guesses Reached?
├─ Yes → Lose
└─ No  → Repeat
```

## Notes

* The player can only enter one alphabetical character at a time.
* Repeated guesses are detected and ignored.
* The game ends when the word is fully revealed or the hangman is completely drawn.
* The word list is stored separately in `wordList.py` for easier management and expansion.

## Project Structure

```text
hangman/
├── hangman.py
├── wordList.py
```

## What I Learned

This project helped me practice organizing code into functions, managing game state, validating user input, working with collections (lists, sets, and dictionaries), and separating data into modules.
