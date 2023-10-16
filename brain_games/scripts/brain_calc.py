#!/usr/bin/env python3
import prompt


import brain_games.games.operations
from brain_games.games import dialogue
from brain_games.games.operations import correct_answer_calc, check_calc, number_generation, ATTEMPTS


def main():
    name = dialogue.welcome_user()
    dialogue.start_calc_game()
    for i in range(ATTEMPTS):
        number1 = number_generation()
        number2 = number_generation()
        operation = brain_games.games.operations.operation_generation()
        print(f"Question: {number1} {operation} {number2}")
        answer = prompt.integer('Your answer: ')
        if not dialogue.checking_answer(answer, name,
                                        check_calc(number1, number2, operation, answer),
                                        correct_answer_calc(number1, number2, operation)):
            break
        if i == 2:
            print(f"Congratulations, {name}!")


if __name__ == '__main__':
    main()
