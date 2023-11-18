#!/usr/bin/env python3
import prompt

import brain_games.games.operations
from brain_games.games import dialogue
from brain_games.games.dialogue import is_right_answer
from brain_games.games.operations import (correct_answer_calc, is_answer_calc,
                                          generate_number)
from brain_games.games.settings import ATTEMPTS


def main():
    name = dialogue.welcome_user()
    dialogue.start_calc_game()
    for i in range(ATTEMPTS):
        number1 = generate_number()
        number2 = generate_number()
        operation = brain_games.games.operations.generate_operation()
        print(f"Question: {number1} {operation} {number2}")
        answer = prompt.integer('Your answer: ')
        answer_calc = is_answer_calc(number1, number2, operation, answer)
        correct_answer = correct_answer_calc(number1, number2, operation)
        if not is_right_answer(answer, name, answer_calc, correct_answer):
            break
        if i == 2:
            print(f"Congratulations, {name}!")


if __name__ == '__main__':
    main()
