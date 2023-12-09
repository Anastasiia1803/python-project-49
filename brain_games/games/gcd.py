import math

from brain_games.engine import run_game
from brain_games.games.constants import MANUAL_GCD
from brain_games.games.utils import get_random_number


def get_result_gcd():
    random_number_1 = get_random_number(to_num=10)
    random_number_2 = get_random_number(to_num=10)
    correct_answer = math.gcd(random_number_1, random_number_2)
    return f'{random_number_1} {random_number_2}', str(correct_answer)


def run_gcd_game():
    run_game(manual=MANUAL_GCD, func_game=get_result_gcd)
