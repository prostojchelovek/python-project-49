#!/usr/bin/env python3
import prompt

from brain_games.games import dialogue
from brain_games.games.dialogue import is_right_answer
from brain_games.games.operations import (correct_answer_even,
                                          is_answer_even, generate_number)
from brain_games.games.settings import ATTEMPTS


def main():
    name = dialogue.welcome_user()
    dialogue.start_even_game()
    for i in range(ATTEMPTS):
        number = generate_number()
        print(f"Question: {number}")
        answer = prompt.string('Your answer: ')
        answer_even = is_answer_even(number, answer)
        correct_answer = correct_answer_even(number)
        if not is_right_answer(answer, name, answer_even, correct_answer):
            break
        if i == 2:
            print(f"Congratulations, {name}!")


if __name__ == '__main__':
    main()
