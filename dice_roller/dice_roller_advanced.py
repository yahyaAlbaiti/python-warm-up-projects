from random import randint

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

num_of_dice = int(input("How many dice?: "))

# List Comprehension
dice = [randint(1, 6) for _ in range(num_of_dice)]

# Horizontal rendering
for line in range(5):
    for die in dice:
        print(dice_art[die][line], end="")
    print()

# Built-in function
print(f"Total: {sum(dice)}")