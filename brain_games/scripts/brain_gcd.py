from brain_games.engine import run_game
from brain_games.games.gcd import gcd, MANUAL


def main():
    run_game(manual=MANUAL, func_game=gcd)


if __name__ == '__main__':
    main()
