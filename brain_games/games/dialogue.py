import prompt


def welcome_user():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")
    return name


def start_even_game():
    print("Answer \"yes\" if the number is even, otherwise answer \"no\".")


def start_prime_game():
    print("Answer \"yes\" if given number is prime. Otherwise answer \"no\".")


def start_calc_game():
    print("What is the result of the expression?")


def start_gcd_game():
    print("Find the greatest common divisor of given numbers.")


def start_progression_game():
    print("What number is missing in the progression?")


def checking_answer(answer, name, check_answer, correct_answer):
    if check_answer:
        print("Correct!")
        return True
    else:
        print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
        print(f"Let's try again, {name}!")
        return False
