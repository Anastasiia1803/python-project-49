import random
from brain_games.engine import get_question_and_answer
from brain_games.constants import OPERATIONS, MANUAL_CALC
from brain_games.games.utils import get_random_number


def get_num_and_calculate_answer():
    operation = random.choice(OPERATIONS)
    number_1 = get_random_number()
    number_2 = get_random_number()

    correct_answer = calculate(operation, number_1, number_2)
    question = f'{number_1} {operation} {number_2}'
    return question, str(correct_answer)


def calculate(operation, number_1, number_2):
    match operation:
        case '+':
            return number_1 + number_2
        case '-':
            return number_1 - number_2
        case _:
            return number_1 * number_2


def run_calc_game():
    get_question_and_answer(
        manual=MANUAL_CALC,
        func_game=get_num_and_calculate_answer
    )
