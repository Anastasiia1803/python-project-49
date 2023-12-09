import random
from brain_games.engine import run_game
from brain_games.games.constants import OPERATIONS, MANUAL_CALC
from brain_games.games.utils import get_random_number


def get_result_calculate():
    operation = random.choice(OPERATIONS)
    random_number_1 = get_random_number()
    random_number_2 = get_random_number()

    correct_answer = calculate(operation, random_number_1, random_number_2)
    question = f'{random_number_1} {operation} {random_number_2}'
    return question, str(correct_answer)


def calculate(operation, number_1, number_2):
    if operation == '+':
        correct_answer = number_1 + number_2
    elif operation == '-':
        correct_answer = number_1 - number_2
    else:
        correct_answer = number_1 * number_2
    return correct_answer


def run_calc_game():
    run_game(manual=MANUAL_CALC, func_game=get_result_calculate)
