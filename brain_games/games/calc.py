import random

import prompt


def calc(name):
    count_correct_answer = 0
    print('What is the result of the expression?')
    operations = ['+', '-', '*']

    for operation in operations:
        random_number_1 = random.randint(1, 30)
        random_number_2 = random.randint(1, 30)
        print(f'Question: {random_number_1} {operation} {random_number_2}')
        answer = prompt.integer('Your answer: ')

        if operation == '+':
            correct_answer = random_number_1 + random_number_2
        elif operation == '-':
            correct_answer = random_number_1 - random_number_2
        else:
            correct_answer = random_number_1 * random_number_2

        if answer == correct_answer:
            print('Correct!')
            count_correct_answer = count_correct_answer + 1
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer"
                  f" was '{correct_answer}'. Let's try again, {name}!")
            break

    if count_correct_answer == 3:
        print(f'Congratulations, {name}!')