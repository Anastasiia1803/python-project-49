from brain_games.engine import run_game
from brain_games.games.calc import calc, MANUAL


def main():
    run_game(manual=MANUAL, func_game=calc)


if __name__ == '__main__':
    main()
