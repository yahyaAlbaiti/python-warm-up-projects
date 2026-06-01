# Rock Paper Scissors 🎮

A simple command-line Rock Paper Scissors game built with Python.

## Features

* Player vs Computer gameplay
* Random computer choices
* Input validation
* Win, loss, and tie tracking
* Win rate and loss rate calculation
* Replay system

## Concepts Practiced

* Variables
* Lists
* Dictionaries
* Loops (`while`)
* Conditional Statements (`if`, `elif`, `else`)
* User Input
* Random Module
* Counters
* Basic Statistics

## How It Works

1. The player enters:

   * rock
   * paper
   * scissors

2. The computer randomly selects one of the available options.

3. The program determines the winner using a dictionary that stores which choice defeats another:

```python
wins_against = {
    "rock": "scissors",
    "paper": "rock",
    "scissors": "paper"
}
```

4. Win, loss, and tie counters are updated.

5. The player can choose to play again.

6. At the end of the session, the program displays:

   * Total wins
   * Total losses
   * Total ties
   * Win rate
   * Loss rate

## Example Output

enter (rock, paper, scissors): rock

player: rock
computer: scissors

player win!!

again? (y/n): y

---

enter (rock, paper, scissors): paper

player: paper
computer: scissors

computer win!!

again? (y/n): n

--------- THANKS FOR PLAYING ------------

you win 1 times
you lose 1 times
you tie 0 times

your win rate is: 50%
your lose rate is: 50%

## What I Learned

* Using dictionaries to simplify game logic
* Validating user input
* Tracking game statistics
* Using loops to create replayable programs
* Generating random choices with Python

## Future Improvements

* Best-of-3 mode
* Best-of-5 mode
* Scoreboard persistence
* GUI version using Tkinter or PyQt
* Multiplayer mode
* Rock Paper Scissors Lizard Spock variation
