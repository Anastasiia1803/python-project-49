import random

import prompt

import math

from brain_games.cli import welcome_user


def main():
    welcome_user()
    print('Find the greatest common divisor of given numbers')

    for i in range(3):
        random_number_1 = random.randint(1, 10)
        random_number_2 = random.randint(1, 10)
        print(f'Question: {random_number_1} {random_number_2}')

        answer = prompt.integer('Your answer: ')
        correct_answer = math.gcd(random_number_1, random_number_2)

        if answer == correct_answer:
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")

if __name__ == '__main__':
    main()