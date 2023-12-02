import random

MANUAL = 'What number is missing in the progression?'


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
