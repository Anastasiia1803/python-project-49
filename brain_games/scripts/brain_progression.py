from brain_games.cli import welcome_user
from brain_games.games.progression import progression


def main():
    name = welcome_user()
    progression(name)


if __name__ == '__main__':
    main()
