#!/usr/bin/env python3
import prompt

from brain_games.games import dialogue
from brain_games.games.operations import (progression_output,
                                          select_progression_element,
                                          progression_generation,
                                          has_progression_element)
from brain_games.games.settings import ATTEMPTS


def main():
    name = dialogue.welcome_user()
    dialogue.start_progression_game()
    for i in range(ATTEMPTS):
        progression = progression_generation()
        element = select_progression_element(progression)
        print(f"Question: {progression_output(progression, element)}")
        answer = prompt.integer('Your answer: ')
        is_right_elem = has_progression_element(element, answer)
        if not dialogue.is_right_answer(answer, name, is_right_elem, element):
            break
        if i == 2:
            print(f"Congratulations, {name}!")


if __name__ == '__main__':
    main()
