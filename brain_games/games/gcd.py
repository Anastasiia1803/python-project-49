import math
import random
from brain_games.engine import run_game
from brain_games.games.constants import MANUAL_GCD


def run_gcd_game():
    run_game(manual=MANUAL_GCD, func_game=gcd)


def gcd():
    random_number_1 = random.randint(1, 10)
    random_number_2 = random.randint(1, 10)
    correct_answer = math.gcd(random_number_1, random_number_2)
    return f'{random_number_1} {random_number_2}', str(correct_answer)
