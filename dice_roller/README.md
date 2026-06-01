# Dice Roller 🎲

A Python command-line application that simulates rolling one or more dice and displays the results using ASCII art.

## Features

### Basic Version

* Generate random dice values
* Store rolls in a list
* Display dice vertically
* Calculate total using an accumulator variable

### Advanced Version

* List comprehension
* Horizontal dice display
* Built-in `sum()` function
* More Pythonic implementation

## Concepts Practiced

* Dictionaries
* Tuples
* Lists
* Loops
* Random Module
* List Comprehension
* ASCII Art
* Built-in Functions
* Nested Loops

## How It Works

1. The user enters the number of dice to roll.

2. Random dice values are generated.

3. Each value is stored in a list.

Example:

```python
dice = [3, 5, 1]
```

4. A dictionary stores the ASCII art representation of each dice face.

Example:

```python
dice_art[5]
```

returns:

```text
┌─────────┐
│ ●     ● │
│    ●    │
│ ●     ● │
└─────────┘
```

5. The program displays all dice.

6. The total value of all rolls is calculated and displayed.

## Example Output

How many dice?: 3

```text
┌─────────┐┌─────────┐┌─────────┐
│ ●       ││ ●     ● ││         │
│    ●    ││    ●    ││    ●    │
│       ● ││ ●     ● ││         │
└─────────┘└─────────┘└─────────┘
```

Total: 9

## Project Structure

```text
dice_roller/
├── dice_roller_basic.py
├── dice_roller_advanced.py
└── README.md
```

## What I Learned

* How dictionaries can store complex data structures
* How nested loops work
* How to display text-based graphics using ASCII art
* The difference between vertical and horizontal rendering
* How list comprehensions simplify code
* How built-in functions such as `sum()` reduce boilerplate code

## Future Improvements

* Colored terminal output
* Dice rolling animation
* Custom dice (D4, D8, D10, D20)
* Graphical user interface (GUI)
* Roll history tracking
* Multiplayer dice game support
