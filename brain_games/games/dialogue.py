import prompt
import brain_games.games.even


def welcome_user():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")
    return name


def start_even_game():
    print("Answer \"yes\" if the number is even, otherwise answer \"no\".")


def checking_answer(number: int, answer: str, name: str, check_answer: bool) -> bool:
    if check_answer:
        print("Correct!")
        return True
    else:
        print(f"'{answer}' is wrong answer ;(. Correct answer was '{brain_games.games.even.correct_answer(number)}'.")
        print(f"Let's try again, {name}!")
        return False
