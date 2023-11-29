from brain_games.engine import run_game
from brain_games.games.progression import progression, MANUAL


def main():
    run_game(manual=MANUAL, func_game=progression)


if __name__ == '__main__':
    main()
