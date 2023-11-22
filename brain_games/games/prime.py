import random

import prompt


def is_prime(x) -> bool:
    for i in range(2, x):
        if x % i == 0:
            return False

    return True


def prime(name):
    count_correct_answer = 0
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    for i in range(3):
        j = random.randint(1, 10)
        print('Question:', j)
        answer = prompt.string('Your answer: ')
        if is_prime(j):
            correct_answer = 'yes'
        else:
            correct_answer = 'no'

        if answer == correct_answer:
            print('Correct!')
            count_correct_answer = count_correct_answer + 1
        else:
            print(f"'{answer}' is wrong answer ;(."
                  f" Correct answer was '{correct_answer}'. Let's try again, {name}!")
    if count_correct_answer == 3:
        print(f'Congratulations, {name}!')
