from brain_games.engine import run_game
from brain_games.games.even import even, MANUAL


def main():
    run_game(manual=MANUAL, func_game=even)


if __name__ == '__main__':
    main()
