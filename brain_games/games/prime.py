from brain_games.engine import get_question_and_answer
from brain_games.constants import MANUAL_PRIME
from brain_games.games.utils import get_random_number


def is_prime(x) -> bool:
    if x <= 1:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False

    return True


def get_num_and_prime_answer():
    number = get_random_number(to_num=10)
    correct_answer = 'yes' if is_prime(number) else 'no'
    return number, correct_answer


def run_prime_game():
    get_question_and_answer(
        manual=MANUAL_PRIME,
        func_game=get_num_and_prime_answer
    )
