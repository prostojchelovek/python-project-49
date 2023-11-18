import prompt

from brain_games.games import dialogue
from brain_games.games.operations import (correct_answer_gcd, check_gcd,
                                          generate_number)
from brain_games.games.settings import ATTEMPTS


def main():
    name = dialogue.welcome_user()
    dialogue.start_gcd_game()
    for i in range(ATTEMPTS):
        number1 = generate_number()
        number2 = generate_number()
        print(f"Question: {number1} {number2}")
        answer = prompt.integer('Your answer: ')
        if not dialogue.checking_answer(answer,
                                        name,
                                        check_gcd(number1, number2, answer),
                                        correct_answer_gcd(number1, number2)):
            break
        if i == 2:
            print(f"Congratulations, {name}!")


if __name__ == '__main__':
    main()
