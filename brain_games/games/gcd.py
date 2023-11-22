import math
import random

import prompt

from brain_games.cli import welcome_user


def gcd(name):
    count_correct_answer = 0
    print('Find the greatest common divisor of given numbers.')

    for i in range(3):
        random_number_1 = random.randint(1, 10)
        random_number_2 = random.randint(1, 10)
        print(f'Question: {random_number_1} {random_number_2}')

        answer = prompt.integer('Your answer: ')
        correct_answer = math.gcd(random_number_1, random_number_2)

        if answer == correct_answer:
            print('Correct!')
            count_correct_answer = count_correct_answer + 1
        else:
            print(f"'{answer}' is wrong answer ;(."
                  f" Correct answer was '{correct_answer}'. Let's try again, {name}!")
            break
    if count_correct_answer == 3:
        print(f'Congratulations, {name}!')
