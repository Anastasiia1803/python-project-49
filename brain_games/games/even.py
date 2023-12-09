from brain_games.engine import run_game
from brain_games.games.constants import MANUAL_EVEN
from brain_games.games.utils import get_random_number


def get_result_even():
    random_number = get_random_number()
    if random_number % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return random_number, correct_answer


def run_even_game():
    run_game(manual=MANUAL_EVEN, func_game=get_result_even)
