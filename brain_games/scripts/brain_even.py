#!/usr/bin/env python3
from brain_games.games import dialogue
from brain_games.games.operations import correct_answer_even, check_even, number_generation, ATTEMPTS
import prompt


def main():
    name = dialogue.welcome_user()
    dialogue.start_even_game()
    for i in range(ATTEMPTS):
        number = number_generation()
        print(f"Question: {number}")
        answer = prompt.string('Your answer: ')
        if not dialogue.checking_answer(answer, name, check_even(number, answer), correct_answer_even(number)):
            break
        if i == 2:
            print(f"Congratulations, {name}!")


if __name__ == '__main__':
    main()
