from brain_games.cli import welcome_user
from brain_games.games.gcd import gcd


def main():
    name = welcome_user()
    gcd(name)


if __name__ == '__main__':
    main()
