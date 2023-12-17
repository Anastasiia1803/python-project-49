from brain_games.engine import get_question_and_answer
from brain_games.constants import MANUAL_EVEN
from brain_games.games.utils import get_random_number


def get_num_and_even_answer():
    number = get_random_number()
    correct_answer = 'yes' if is_even(number) else 'no'
    return number, correct_answer


def is_even(number):
    return number % 2 == 0


def run_even_game():
    get_question_and_answer(
        manual=MANUAL_EVEN,
        func_game=get_num_and_even_answer
    )
