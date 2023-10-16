import random


def check(number, answer):
    if correct_answer(number) == answer:
        return True
    return False


def correct_answer(number):
    if number % 2 == 0:
        return 'yes'
    else:
        return'no'


def number_generation():
    return random.randint(1, 100)
