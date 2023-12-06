import random
from brain_games.engine import run_game
from brain_games.games.constants import MANUAL_PROGRESSION


def run_progression_game():
    run_game(manual=MANUAL_PROGRESSION, func_game=progression)


def progression():
    start = random.randint(0, 50)
    step = random.randint(2, 10)
    a = []
    for k in range(10):
        a.append(start)
        start = start + step

    random_ind = random.randint(1, 9)

    correct_answer = a.pop(random_ind)
    a.insert(random_ind, '..')
    c = []
    for x in a:
        c.append(str(x))

    h = ' '.join(c)
    return h, str(correct_answer)
