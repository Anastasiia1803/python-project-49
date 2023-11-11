import random

import prompt

import math


def progression():
    print('What number is missing in the progression?')
    for i in range(3):
        start = random.randint(0, 50)
        step = random.randint(2, 10)
        a = []
        for k in range(10):
            a.append(start)
            start = start + step

        random_ind = random.randint(1,9)

        random_num = a.pop(random_ind)
        a.insert(random_ind, '..')
        c = []
        for x in a:
            c.append(str(x))

        h = ' '.join(c)

        print('Question:', h)

        answer = prompt.integer('Your answer: ')

        if answer == random_num:
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{random_num}'.")
            print("Let's try again, Sam!")

    print('Congratulations, Sam!')


progression()





