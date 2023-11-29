import random

MANUAL = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(x) -> bool:
    for i in range(2, x):
        if x % i == 0:
            return False

    return True


def prime():
    j = random.randint(1, 10)
    if is_prime(j):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'

    return j, correct_answer
