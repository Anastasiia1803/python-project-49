import random
from brain_games.engine import run_game
from brain_games.games.constants import OPERATIONS, MANUAL_CALC


def run_calc_game():
    run_game(manual=MANUAL_CALC, func_game=calculate)


def calculate():
    operation = random.choice(OPERATIONS)
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
