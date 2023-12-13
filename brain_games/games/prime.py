from brain_games.engine import run_game
from brain_games.games.constants import MANUAL_PRIME
from brain_games.games.utils import get_random_number


def is_prime(x) -> bool:
    if x <= 1:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False

    return True


def get_result_prime():
    j = get_random_number(to_num=10)
    if is_prime(j):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'

    return j, correct_answer


def run_prime_game():
    run_game(manual=MANUAL_PRIME, func_game=get_result_prime)
