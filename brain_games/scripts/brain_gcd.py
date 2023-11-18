import prompt

from brain_games.games import dialogue
from brain_games.games.dialogue import is_right_answer
from brain_games.games.operations import (correct_answer_gcd, is_answer_gcd,
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
        answer_gcd = is_answer_gcd(number1, number2, answer)
        correct_answer = correct_answer_gcd(number1, number2)
        if not is_right_answer(answer, name, answer_gcd, correct_answer):
            break
        if i == 2:
            print(f"Congratulations, {name}!")


if __name__ == '__main__':
    main()
