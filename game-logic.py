import random

WORDS = ["питон", "виселица", "компьютер", "программа", "алгоритм", "игра", "комната", "линукс"]

def choose_word():
    return random.choice(WORDS)

def display_current_state(guessed_word):
    print("Слово: " + " ".join(guessed_word))

def main():
    secret_word = choose_word()
    guessed_word = ["_"] * len(secret_word)
    attempts_left = 8
    guessed_letters = set()

    print("Добро пожаловать в игру 'Виселица'!")
    print("У вас есть", attempts_left, "попыток.")

    while attempts_left > 0 and "_" in guessed_word:
        display_current_state(guessed_word)
        guess = input("Введите букву: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Пожалуйста, введите одну букву.")
            continue

        if guess in guessed_letters:
            print("Вы уже пробовали эту букву.")
            continue

        guessed_letters.add(guess)

        if guess in secret_word:
            for i, letter in enumerate(secret_word):
                if letter == guess:
                    guessed_word[i] = guess
            print("Верно!")
        else:
            attempts_left -= 1
            print("Неверно! Осталось попыток:", attempts_left)

    if "_" not in guessed_word:
        print("Поздравляем! Вы угадали слово:", secret_word)
    else:
        print("Вы проиграли. Загаданное слово было:", secret_word)

if __name__ == "__main__":
    main()