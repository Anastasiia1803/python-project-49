from brain_games.engine import get_question_and_answer
from brain_games.constants import MANUAL_PROGRESSION
from brain_games.games.utils import get_random_number


def get_num_and_progression_answer():
    start = get_random_number()
    step = get_random_number(1, 10)

    progression = get_progression(start, step)
    random_ind = get_random_number(1, 9)
    correct_answer = progression.pop(random_ind)
    progression.insert(random_ind, '..')
    return ' '.join(map(str, progression)), str(correct_answer)


def get_progression(start, step):
    a = []
    for k in range(10):
        a.append(start)
        start = start + step
    return a


def run_progression_game():
    get_question_and_answer(
        manual=MANUAL_PROGRESSION,
        func_game=get_num_and_progression_answer
    )
