from brain_games.cli import welcome_user
from brain_games.games.even import even


def main():
    name = welcome_user()
    even(name)


if __name__ == '__main__':
    main()
