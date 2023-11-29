from brain_games.engine import run_game
from brain_games.games.prime import prime, MANUAL


def main():
    run_game(manual=MANUAL, func_game=prime)


if __name__ == '__main__':
    main()
