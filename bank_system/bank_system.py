from datetime import datetime

def show_balance(current_balance):
    print(f"\n---- Your balance is ${current_balance:.2f} ----")


def deposit(balance, transactions):
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M")

    try:
        amount = float(input("\nEnter how much do you want to deposit: "))
    except ValueError:
        print("Please enter a valid number.")
        return balance

    if amount <= 0:
        print("you can't deposit less than 1")
        return balance

    balance += amount
    print("\ndeposit successful!")
    print(f"---- your new balance is ${balance:.2f} ----")

    transactions.append({
        "type": "deposit",
        "amount": amount,
        "time": current_time
    })
    return balance


def withdraw(balance, transactions):
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M")
    try:
        amount = float(input("\nEnter how much you want to withdraw: "))
    except ValueError:
        print("Please enter a valid number.")
        return balance

    if amount > balance:
        print("Can't withdraw more than your balance.")
    elif amount <= 0:
        print("You can't withdraw less than 0!")
    else:
        balance -= amount
        print("\nWithdrawal successful!")
        print(f"---- your new balance is ${balance:.2f} ----")

        transactions.append({
            "type": "withdrawal",
            "amount": amount,
            "time": current_time
        })
    return balance


def show_transactions(transactions):
    if not transactions:
        print("No history found.")
        return

    for i, transaction in enumerate(transactions, start=1):
        print(
            f"{i}. "
            f"{transaction['type'].capitalize():<12}"
            f"${transaction['amount']:<10.2f}"
            f"{transaction['time']}"
        )

def main():
    balance = 0
    running = True
    transactions = []

    while running:
        print("""
1. Show Balance
2. Deposit
3. Withdraw
4. Transaction History
5. Exit
""")

        choice = input("Enter number from menu: ")

        if choice == '1':
            show_balance(balance)

        elif choice == '2':
            balance = deposit(balance, transactions)

        elif choice == '3':
            balance = withdraw(balance, transactions)

        elif choice == '4':
            print("\n---------- Transaction History -----------")
            show_transactions(transactions)

        elif choice == '5':
            running = False

        else:
            print("Invalid choice.")

    print("\n------ Thank You ------")

    total_deposits = sum(
        t["amount"]
        for t in transactions
        if t["type"] == "deposit"
    )

    total_withdrawals = sum(
        t["amount"]
        for t in transactions
        if t["type"] == "withdrawal"
    )

    print(f"Total deposits: ${total_deposits:.2f}")
    print(f"Total withdrawals: ${total_withdrawals:.2f}")
    print(f"Current balance: ${balance:.2f}")


if __name__ == '__main__':
    main()