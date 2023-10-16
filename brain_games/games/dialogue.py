import prompt


def welcome_user():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")
    return name


def start_even_game():
    print("Answer \"yes\" if the number is even, otherwise answer \"no\".")


def start_calc_game():
    print("What is the result of the expression?")


def checking_answer(answer, name: str, check_answer: bool, correct_answer) -> bool:
    if check_answer:
        print("Correct!")
        return True
    else:
        print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
        print(f"Let's try again, {name}!")
        return False
