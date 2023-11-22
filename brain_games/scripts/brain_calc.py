from brain_games.cli import welcome_user
from brain_games.games.calc import calc


def main():
    name = welcome_user()
    calc(name)


if __name__ == '__main__':
    main()
