import random

options =("rock", "paper", "scissors")
wins_against = {
    "rock": "scissors",
    "paper": "rock",
    "scissors": "paper"
}
win_counter = 0
lose_counter = 0
tie_counter = 0
running = True

while running:
    player = None

    while player not in options:
        player = input("enter (rock, paper, scissors): ").lower()

    computer = random.choice(options)

    print(f"player: {player}")
    print(f"computer: {computer}")

    if wins_against[player] == computer: 
        print("player win!!")
        win_counter +=1

    elif player == computer:
        print("it's a tie!!")
        tie_counter +=1

    else:
        print("computer win!!")
        lose_counter +=1

    if not input("again? (y/n): ").lower() == 'y':
        running = False
    print("------------")

print("--------- THANKS FOR PLAYING ------------")
print(f"you win {win_counter} times")
print(f"you lose {lose_counter} times")
print(f"you tie {tie_counter} times")
total = win_counter + lose_counter + tie_counter
win_rate = int((win_counter/total) * 100)
lose_rate = int((lose_counter/total)*100)
print(f"your win rate is: {round(win_rate)}%")
print(f"your lose rate is: {round(lose_rate)}%")