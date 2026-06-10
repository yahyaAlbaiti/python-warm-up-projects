# Slot Machine

## Description

A simple Python slot machine game where the player places bets, spins the reels, and wins payouts when all three symbols match.

The game tracks the player's balance, validates bets, calculates winnings, and displays the total profit or loss at the end of the session.

## Features

* Place bets using your current balance
* Random slot machine spins
* Different payout multipliers for each symbol
* Input validation for bets
* Balance tracking
* Profit/Loss tracking
* Play multiple rounds

## Concepts Practiced

* Functions
* Lists
* Dictionaries
* List comprehensions
* Input validation
* Loops
* Conditional statements
* Constants
* Random module

## How It Works

1. Start with an initial balance.
2. Enter a valid bet amount.
3. Spin the slot machine.
4. Check if all three symbols match.
5. Calculate winnings based on the matching symbol.
6. Update balance and profit.
7. Continue playing or exit the game.
8. Display final profit or loss.

## Example

```text
---- Welcome To Machine Slot ----

your current balance is $100
enter your bet: 10

Spinning...

🍒 | 🍒 | 🍒

--- YOU WIN $50 ---

do you want to play again? (y/n):
```

## Payout Table

| Symbol | Multiplier |
| ------ | ---------- |
| 🍋     | x3         |
| 🍉     | x4         |
| 🍒     | x5         |
| 🔔     | x10        |
| ⭐      | x20        |

## Project Flow


```text
Start
  ↓
Set Initial Balance
  ↓
Enter Bet
  ↓
Validate Bet
  ↓
Spin Slot Machine
  ↓
Display Symbols
  ↓
Check Matching Symbols
  ↓
Calculate Payout
  ↓
Update Balance & Profit
  ↓
Play Again?
├─ Yes → Enter Bet
└─ No
     ↓
Display Profit/Loss
     ↓
End Game
```


## Notes

* A payout is awarded only when all three symbols match.
* The game ends when the player chooses to quit or runs out of money.
* Profit tracking shows whether the player finished with a gain or a loss.
