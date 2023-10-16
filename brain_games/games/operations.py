import random
import operator


ATTEMPTS = 3
ops = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
}


def check_even(number, answer):
    if correct_answer_even(number) == answer:
        return True
    return False


def check_calc(number1, number2, operation, answer):
    if correct_answer_calc(number1, number2, operation) == answer:
        return True
    return False


def check_gcd(number1, number2, answer):
    if correct_answer_gcd(number1, number2) == answer:
        return True
    return False


def correct_answer_even(number):
    if number % 2 == 0:
        return 'yes'
    else:
        return'no'


def correct_answer_gcd(number1, number2):
    while number1 > 0 and number2 > 0:
        if number1 >= number2:
            number1 = number1 % number2
        else:
            number2 = number2 % number1
    return max(number1, number2)


def number_generation():
    return random.randint(1, 100)


def operation_generation():
    return random.choice("+-*")


def correct_answer_calc(number1, number2, operation):
    return ops[operation](number1, number2)
