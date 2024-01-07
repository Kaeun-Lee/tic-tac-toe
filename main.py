from game import TicTacToeGame
import argparse


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
    args = parser.parse_args()
    return args


def main() -> None:
    game = TicTacToeGame(get_args().num_players)
    game.run()


if __name__ == "__main__":
    main()
