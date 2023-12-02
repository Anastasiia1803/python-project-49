import random

MANUAL = 'What is the result of the expression?'


def calc():
    operations = ['+', '-', '*']
    operation = random.choice(operations)
    random_number_1 = random.randint(1, 30)
    random_number_2 = random.randint(1, 30)

    if operation == '+':
        correct_answer = random_number_1 + random_number_2
    elif operation == '-':
        correct_answer = random_number_1 - random_number_2
    else:
        correct_answer = random_number_1 * random_number_2
    question = f'{random_number_1} {operation} {random_number_2}'
    return question, str(correct_answer)
