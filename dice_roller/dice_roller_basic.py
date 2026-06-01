import random

# Dictionary:
# key   -> dice number
# value -> ASCII art representing that dice face
dice_art = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│ ●       │",
        "│         │",
        "│       ● │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│ ●       │",
        "│    ●    │",
        "│       ● │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│ ●     ● │",
        "│         │",
        "│ ●     ● │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│ ●     ● │",
        "│    ●    │",
        "│ ●     ● │",
        "└─────────┘"),
    6: ("┌─────────┐",
        "│ ●     ● │",
        "│ ●     ● │",
        "│ ●     ● │",
        "└─────────┘")
}

dice = []      # Store generated dice values
total = 0      # Accumulator variable

num_of_dice = int(input("How many dice?: "))

# Generate random dice values and store them in a list
for die in range(num_of_dice):
    dice.append(random.randint(1, 6))

# Display dice vertically
for die in range(num_of_dice):
    for line in dice_art.get(dice[die]):
        print(line)

# Calculate total using accumulator pattern
for die in dice:
    total += die

print(f"total: {total}")