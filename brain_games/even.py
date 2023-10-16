import random


def check(number, answer):
    if number % 2 == 0 and answer == 'yes':
        return True
    elif number % 2 != 0 and answer == 'no':
        return True
    return False


def number_generation():
    return random.randint(1, 100)
