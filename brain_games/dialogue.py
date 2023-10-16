import prompt
import brain_games.even


def welcome_user():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")
    return name


def start_even_game():
    print("Answer \"yes\" if the number is even, otherwise answer \"no\".")


def checking_answer(name: str):
    number = brain_games.even.number_generation()
    print(f"Question: {number}")
    answer = prompt.string('Your answer: ')
    if brain_games.even.check(number, answer):
        print("Correct!")
        return True
    else:
        print(f"'yes' is wrong answer ;(. Correct answer was 'no'.\nLet's try again, {name}!")
        return False
