import random

import prompt


def is_prime(x) -> bool:
    for i in range(2, x):
        if x % i == 0:
            return False

    return True


def prime():
    print('Welcome to the Brain Games!\nHello, Sam!\nAnswer "yes" if given number is prime. Otherwise answer "no".')
    j = random.randint(1, 10)
    print('Question:', j)
    answer = prompt.string('Your answer: ')
    if is_prime(j):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'

    if answer == correct_answer:
        print('Correct!')
    else:
        print('Incorrect!')

prime()