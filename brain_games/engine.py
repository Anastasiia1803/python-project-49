import prompt

COUNT_GAMES = 3


def run_game(manual, func_game):
    name = prompt.string('Welcome to the Brain Games!\nMay I have your name? ')
    print(f'Hello, {name}!\n{manual}')
    for _ in range(COUNT_GAMES):
        question, correct_answer = func_game()
        user_answer = prompt.string(f'Question: {question}\nYour answer: ')
        if user_answer == correct_answer:
            print('Correct!')
        else:
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'. "
                  f"Let's try again, {name}!")
            return

    print(f'Congratulations, {name}!')
