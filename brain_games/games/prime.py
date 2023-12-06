import random
from brain_games.engine import run_game
from brain_games.games.constants import MANUAL_PRIME


def run_prime_game():
    run_game(manual=MANUAL_PRIME, func_game=prime)


def is_prime(x) -> bool:
    for i in range(2, x):
        if x % i == 0:
            return False

    return True


def prime():
    j = random.randint(1, 10)
    if is_prime(j):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'

    return j, correct_answer
