from random import choice
from wordList import words

hangman_art = {
    0: ("   ", "   ", "   "),
    1: ("   O ", "   ", "   "),
    2: ("   O ", "   | ", "   "),
    3: ("   O ", "  /| ", "   "),
    4: ("   O ", "  /|\\", "   "),
    5: ("   O ", "  /|\\", "  /  "),
    6: ("   O ", "  /|\\", "  / \\")
}

def display_man(wrong_guess):
    for line in hangman_art[wrong_guess]:
        print(line)

def display_hint(hint):
    print(" ".join(hint))

def display_answer(answer):
    print("the answer is: ",end="")
    print(" ".join(answer))

def main():
    answer = choice(words)
    hint = ["_"] * len(answer)
    wrong_guess = 0
    is_running = True
    guessed = set()
    remaining_guesses = 6

    while is_running:
        print("---------")
        display_man(wrong_guess)
        print("---------")
        display_hint(hint)

        guess = input("enter letter to guess: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input")
            continue

        if guess in guessed:
            print("letter already used!")
            continue

        guessed.add(guess)

        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess
        else:
            wrong_guess += 1
            remaining_guesses -= 1
            print(f"{remaining_guesses} guess left")

        if "_" not in hint:
            print("---------")
            display_man(wrong_guess)
            print("---------")
            display_answer(answer)
            print("---- YOU WON! ----")
            is_running = False

        elif wrong_guess >= len(hangman_art) -1 :
            print("---------")
            display_man(wrong_guess)
            print("---------")
            display_answer(answer)
            print("---- YOU LOSE! ----")
            is_running = False

if __name__ == '__main__':
    main()