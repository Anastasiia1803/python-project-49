import random
from brain_games.engine import run_game
from brain_games.games.constants import MANUAL_EVEN


def run_even_game():
    run_game(manual=MANUAL_EVEN, func_game=even)


def even():
    random_number = random.randint(1, 100)
    if random_number % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return random_number, correct_answer
