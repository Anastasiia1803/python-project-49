from brain_games.cli import welcome_user
from brain_games.games.prime import prime


def main():
    name = welcome_user()
    prime(name)


if __name__ == '__main__':
    main()
