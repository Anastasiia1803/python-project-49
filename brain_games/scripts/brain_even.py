import random
import prompt


def parity_check():
    while True:
        random_number = random.randint(1, 100)
        print('Answer "yes" if the number is even, otherwise answer "no".')
        print(f'Question: {random_number}')
        answer = prompt.string('Your answer: ')
        if random_number % 2 == 0:
            correct_answer = 'yes'
        else:
            correct_answer = 'no'




        if answer == correct_answer:
            print('Correct!')
            break
        else:
            print("'yes' is wrong answer ;(. Correct answer was 'no'. Let's try again, Bill!")

parity_check()