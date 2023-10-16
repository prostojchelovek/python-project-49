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


def correct_answer_even(number):
    if number % 2 == 0:
        return 'yes'
    else:
        return'no'


def number_generation():
    return random.randint(1, 100)


def operation_generation():
    return random.choice("+-*")


def correct_answer_calc(number1, number2, operation):
    return ops[operation](number1, number2)
