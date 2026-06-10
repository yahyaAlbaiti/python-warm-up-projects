from random import choice

SYMBOLS = ['🍋', '🍉', '🍒', '🔔', '⭐']
PAYOUT = {
        '🍋': 3,
        '🍉': 4,
        '🍒': 5,
        '🔔': 10,
        '⭐': 20
    }

def spin(symbols):
    return [choice(symbols) for _ in range(3)]

def print_row(row):
    print(" | ".join(row))

def get_payout(row, bet, payout):
    if row[0] == row[1] == row[2]:
        return payout[row[0]] * bet

    return 0

def get_bet(balance):
    bet = input("enter your bet: ")

    if not bet.isdigit():
        print("Invalid input")
        return None

    bet = int(bet)
    if bet <= 0:
        print("bet can't be less than zero")
        return None

    if bet > balance:
        print("bet is bigger than your balance")
        return None

    return bet

def main():
    balance = 100
    total_profit = 0

    print("---- Welcome To Machine Slot ----")
    print("symbols are: 🍋, 🍉, 🍒, 🔔, ⭐")

    while True:
        print(f"\nyour current balance is ${balance}")

        bet = get_bet(balance)
        if bet is None:
            continue

        balance -= bet
        total_profit -= bet

        row = spin(SYMBOLS)
        print("Spinning...\n")
        print_row(row)

        payout = get_payout(row, bet, PAYOUT)
        if payout > 0:
            print(f"--- YOU WIN ${payout} ---")
        else:
            print(f"--- YOU LOSE ${bet} ---")

        balance += payout
        total_profit += payout

        if balance <= 0:
            print("sorry your out of money!! ")
            break

        if input("do you want to play again? (y/n): ").lower() != 'y':
            break

    print("\n---- GAME OVER ----")
    if total_profit > 0:
        print(f"Total Profit: +${total_profit} 🤑")
    elif total_profit < 0:
        print(f"Total Profit: -${abs(total_profit)} 📉")
    else:
        print("Total Profit: $0 (You broke even!)")

    print("THANK YOU FOR PLAYING")

if __name__ == '__main__':
    main()