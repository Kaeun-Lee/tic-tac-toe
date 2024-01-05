from game import TicTacToeGame
import argparse


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Configure the settings for the TicTacToe game"
    )
    parser.add_argument(
        "--num_players",
        type=int,
        default=1,
        help="Set the number of players for the game.",
    )
    args = parser.parse_args()
    num_players = args.num_players

    game = TicTacToeGame(num_players)
    game.run()


if __name__ == "__main__":
    main()
