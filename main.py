import argparse

from game import Game


def get_arguments() -> argparse.Namespace:
    """
    Parse command line arguments.

    Return:
        args: Namespace containing user-defined arguments.
    """
    parser = argparse.ArgumentParser(
        description="Configure the settings for the Tic Tac Toe game"
    )
    parser.add_argument(
        "-n",
        "--num_players",
        type=int,
        choices=[1, 2],
        default=1,
        help="set the number of players for the game",
    )
    parser.add_argument(
        "-l",
        "--language",
        type=str,
        choices=["en", "ko"],
        default="ko",
        help="choose the language version for the game.'en' for English, 'ko' for Korean",
    )
    args = parser.parse_args()
    return args


def main() -> None:
    args = get_arguments()
    game = Game(args.num_players, args.language)
    game.run()


if __name__ == "__main__":
    main()
