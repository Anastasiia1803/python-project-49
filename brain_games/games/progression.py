import random

import prompt


def progression(name):
    count_correct_answer = 0
    print('What number is missing in the progression?')
    for i in range(3):
        start = random.randint(0, 50)
        step = random.randint(2, 10)
        a = []
        for k in range(10):
            a.append(start)
            start = start + step

        random_ind = random.randint(1, 9)

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
            count_correct_answer = count_correct_answer + 1
        else:
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was '{random_num}'. "
                  f"Let's try again, {name}!")
            break
    if count_correct_answer == 3:
        print(f'Congratulations, {name}!')
