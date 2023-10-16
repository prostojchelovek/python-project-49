#!/usr/bin/env python3
from brain_games.games import dialogue
from brain_games.games import even
import prompt


ATTEMPTS = 3


def main():
    name = dialogue.welcome_user()
    dialogue.start_even_game()
    for i in range(ATTEMPTS):
        number = even.number_generation()
        print(f"Question: {number}")
        answer = prompt.string('Your answer: ')
        if not dialogue.checking_answer(number, answer, name, even.check(number, answer)):
            break
        if i == 2:
            print(f"Congratulations, {name}!")


if __name__ == '__main__':
    main()
