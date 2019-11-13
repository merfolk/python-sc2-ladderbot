from __init__ import run_ladder_game
from example_bot import ExampleBot

bot = ExampleBot()


def main():
    print("Starting ladder game...")
    result, opponent_id = run_ladder_game(bot)
    print(result, " against opponent ", opponent_id)


if __name__ == '__main__':
    main()
