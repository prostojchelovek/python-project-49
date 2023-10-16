#!/usr/bin/env python3
from brain_games.games import dialogue
from brain_games.games.operations import (correct_answer_prime, check_prime,
                                          generate_number, ATTEMPTS)
import prompt


def main():
    name = dialogue.welcome_user()
    dialogue.start_prime_game()
    for i in range(ATTEMPTS):
        number = generate_number()
        print(f"Question: {number}")
        answer = prompt.string('Your answer: ')
        if not dialogue.checking_answer(answer,
                                        name,
                                        check_prime(number, answer),
                                        correct_answer_prime(number)):
            break
        if i == 2:
            print(f"Congratulations, {name}!")


if __name__ == '__main__':
    main()
