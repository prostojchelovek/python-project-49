import random
from brain_games.games.settings import NUMBER_OF_ELEMENTS, OPS


def is_answer_even(number, answer):
    if correct_answer_even(number) == answer:
        return True


def is_answer_prime(number, answer):
    if correct_answer_prime(number) == answer:
        return True


def is_answer_calc(number1, number2, operation, answer):
    if correct_answer_calc(number1, number2, operation) == answer:
        return True


def is_answer_gcd(number1, number2, answer):
    if correct_answer_gcd(number1, number2) == answer:
        return True


def has_progression_element(element, answer):
    return element == answer


def correct_answer_even(number):
    if number % 2 == 0:
        return 'yes'
    else:
        return 'no'


def correct_answer_gcd(number1, number2):
    while number1 > 0 and number2 > 0:
        if number1 >= number2:
            number1 = number1 % number2
        else:
            number2 = number2 % number1
    return max(number1, number2)


def generate_number(first=1, second=100):
    return random.randint(first, second)


def generate_operation():
    return random.choice("+-*")


def progression_output(progression, deleted_element):
    str_progression = ""
    for el in progression:
        if el != deleted_element:
            str_progression += str(el) + " "
        else:
            str_progression += '..' + " "
    return str_progression


def select_progression_element(progression):
    return progression[generate_number(0, len(progression) - 1)]


def progression_generation():
    min_progression_el = generate_number(1, 60)
    step = generate_number(2, 6)
    max_progression_el = min_progression_el + step * NUMBER_OF_ELEMENTS
    return range(min_progression_el, max_progression_el, step)


def correct_answer_calc(number1, number2, operation):
    return OPS[operation](number1, number2)


def correct_answer_prime(number):
    if is_prime_number(number):
        return 'yes'
    else:
        return 'no'


def is_prime_number(number):
    if number == 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0 or number == 1:
            return False
    return True
