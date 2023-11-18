#!/usr/bin/env python3
import prompt

from brain_games.games import dialogue
from brain_games.games.operations import (progression_output,
                                          select_progression_element,
                                          progression_generation,
                                          check_progression_element)
from brain_games.games.settings import ATTEMPTS


def main():
    name = dialogue.welcome_user()
    dialogue.start_progression_game()
    for i in range(ATTEMPTS):
        progression = progression_generation()
        element = select_progression_element(progression)
        print(f"Question: {progression_output(progression, element)}")
        answer = prompt.integer('Your answer: ')

        if not dialogue.checking_answer(answer,
                                        name,
                                        check_progression_element(element,
                                                                  answer),
                                        element):
            break
        if i == 2:
            print(f"Congratulations, {name}!")


if __name__ == '__main__':
    main()
