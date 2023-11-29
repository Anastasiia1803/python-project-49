import prompt


def run_game(manual, func_game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(manual)
    count_correct_answer = 0
    for i in range(3):
        res = func_game()
        question = res[0]
        correct_answer = res[1]
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')
        if answer == correct_answer:
            print('Correct!')
            count_correct_answer = count_correct_answer + 1
        else:
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'. "
                  f"Let's try again, {name}!")
            break

        if count_correct_answer == 3:
            print(f'Congratulations, {name}!')
