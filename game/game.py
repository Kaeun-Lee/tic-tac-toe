import random
from itertools import cycle

from board import Board
from player import Computer, Human


class TicTacToeGame:
    """Represents a game of Tic Tac Toe."""

    def __init__(self) -> None:
        players = [Human("player1"), Computer("computer")]
        random.shuffle(players)
        self.first_player = players[0]
        self.second_player = players[1]
        self.rounds_count = 1

    def restart_game(self) -> bool:
        """
        Prompts the player to restart game.

        Return:
            True for restart, False otherwise.
        """
        while True:
            play_again = input("게임을 다시 하시겠습니까? (y/n) : ")
            print()
            if play_again in ["y", "n"]:
                break
            else:
                print("잘못된 값을 입력했습니다. y/n 중 하나를 입력해 주세요.\n")
        return play_again == "y"

    def play_one_round(self, board: Board) -> None:
        """
        Runs a game of Tic Tac Toe between two players.

        Args:
            board: The game board in this round.
        """
        # Display initial game board
        print(board)

        print(f"첫 번째 플레이어는 {self.first_player.name} (O)입니다.")
        print(f"두 번째 플레이어는 {self.second_player.name} (X)입니다.\n")

        symbol_player_pairs = cycle(
            [("O", self.first_player), ("X", self.second_player)]
        )

        for _ in range(len(board._current_state)):
            symbol, current_player = next(symbol_player_pairs)
            move = current_player.select_move(board.get_available_moves())

            board.apply_turn(move, symbol)

            # Updated game board
            print(board)

            if board.is_finished():
                print(
                    f"{current_player.name}님 축하합니다!!! {current_player.name}님이 이겼습니다.\n"
                )
                return
        # Board is full, draw game
        print("비겼습니다. 게임을 다시 시작해 보세요.\n")

    def run(self):
        """Executes the Tic Tac Toe Game."""
        print("#" * 60)
        print(f"{'Tic Tac Toe 게임에 오신 걸 환영합니다!':^50}")
        print("#" * 60)

        print(
            """
        게임 방식을 선택해 주세요.
        (1) 1 PLAYER
        (2) 2 PLAYER\n"""
        )

        print(f"{' Tic Tac Toe 게임을 시작합니다. ':*^52}\n")

        # Initialize variables and start playing game
        board = Board()

        while True:
            print(f'"Round {self.rounds_count}"\n')
            self.play_one_round(board)
            if self.restart_game():
                self.rounds_count += 1
                board.reset()
                self.first_player, self.second_player = (
                    self.second_player,
                    self.first_player,
                )
            else:
                break
        print(f"{' Tic Tac Toe 게임을 종료합니다. ':*^52}\n")
