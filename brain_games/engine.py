import prompt
from brain_games.constants import (
    WELCOME_MESSAGE, QUESTION_MESSAGE, INSTRUCTION)

COUNT_GAMES = 3


def get_question_and_answer(manual, func_game):
    name = prompt.string(WELCOME_MESSAGE)
    print(f'Hello, {name}!', f'{manual}', sep='\n')
    for _ in range(COUNT_GAMES):
        question, correct_answer = func_game()
        user_answer = prompt.string(QUESTION_MESSAGE.format(question))
        if user_answer == correct_answer:
            print('Correct!')
        else:
            print(INSTRUCTION.format(user_answer, correct_answer, name))
            return

    print(f'Congratulations, {name}!')
