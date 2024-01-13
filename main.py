import argparse

from game import TicTacToeGame


def get_args() -> argparse.Namespace:
    """
    Parse command line arguments.

    Return:
        args: The namespace containing user-defined arguments.
    """
    parser = argparse.ArgumentParser(
        description="Configure the settings for the Tic Tac Toe game"
    )
    parser.add_argument(
        "--num_players",
        type=int,
        default=1,
        help="Set the number of players for the game.",
    )
    parser.add_argument(
        "--language",
        type=str,
        default="ko",
        help="Choose the language version for the game. 'en' for English, 'ko' for Korean.",
    )
    args = parser.parse_args()
    return args


def main() -> None:
    args = get_args()
    game = TicTacToeGame(args.num_players, args.language)
    game.run()


if __name__ == "__main__":
    main()
