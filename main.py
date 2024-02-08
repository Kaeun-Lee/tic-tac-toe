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
        help="Set the number of players for the game",
    )
    parser.add_argument(
        "-l",
        "--language",
        type=str,
        choices=["en", "ko"],
        default="ko",
        help="Choose the language version for the game.'en' for English, 'ko' for Korean",
    )
    parser.add_argument(
        "-f",
        "--formatting",
        type=int,
        nargs="*",
        default=None,
        help="Customize formatting widths for messages: [line_width, name_display_width, score_display_width]",
    )
    args = parser.parse_args()
    return args


def main() -> None:
    args = get_arguments()
    if args.formatting == None:
        args.formatting = [60, 20, 10]
    game = Game(args.num_players, args.language, args.formatting)
    game.run()


if __name__ == "__main__":
    main()
