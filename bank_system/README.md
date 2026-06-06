# Banking System

A simple command-line banking application built with Python.

## Features

* Show current account balance
* Deposit funds
* Withdraw funds
* View transaction history
* Track transaction timestamps
* Display deposit and withdrawal statistics when exiting

## Concepts Practiced

* Functions
* Lists
* Dictionaries
* Loops
* Conditional statements
* Input validation
* Exception handling (`try` / `except`)
* Date and time handling with `datetime`
* List comprehensions
* Generator expressions
* The `main()` function pattern

## Example Menu

```text
1. Show Balance
2. Deposit
3. Withdraw
4. Transaction History
5. Exit
```

## Example Transaction Record

```python
{
    "type": "deposit",
    "amount": 100.0,
    "time": "2026-06-06 10:30"
}
```

## What I Learned

* How to organize a program using multiple functions
* How to store structured data using dictionaries
* How to track transaction history
* How to update and return values between functions
* How to validate user input and handle errors gracefully

## Future Improvements

- Save transactions to a file
- Load transaction history when the program starts
- Support multiple bank accounts
- Add account login functionality