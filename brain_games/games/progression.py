from brain_games.engine import run_game
from brain_games.games.constants import MANUAL_PROGRESSION
from brain_games.games.utils import get_random_number


def get_result_progression():
    start = get_random_number()
    step = get_random_number(1, 10)
    a = []
    for k in range(10):
        a.append(start)
        start = start + step

    random_ind = get_random_number(1, 9)

    correct_answer = a.pop(random_ind)
    a.insert(random_ind, '..')
    c = []
    for x in a:
        c.append(str(x))

    h = ' '.join(c)
    return h, str(correct_answer)


def run_progression_game():
    run_game(manual=MANUAL_PROGRESSION, func_game=get_result_progression)
