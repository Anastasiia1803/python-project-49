import math
import random

MANUAL = 'Find the greatest common divisor of given numbers.'


def gcd():
    random_number_1 = random.randint(1, 10)
    random_number_2 = random.randint(1, 10)
    correct_answer = math.gcd(random_number_1, random_number_2)
    return f'{random_number_1} {random_number_2}', correct_answer
