import random
from itertools import cycle

from board import Board
from player import Computer, Human, Player


class TicTacToeGame:
    def __init__(self, num_players: int) -> None:
        """
        Represents a game of Tic Tac Toe.

        Arg:
            num_players: The number of players chosen by the user.
        """
        self.player1, self.player2 = self.set_players(num_players)
        self.rounds_count = 1
        self.board = Board()

    def set_players(self, num_players: int) -> tuple[Player, Player]:
        """
        Sets up players based on the number of players.

        Arg:
            num_players: The number of players chosen by the user.

        Returns:
            The two Player objects.
        """
        if num_players == 1:
            players = [Human("Player 1"), Computer("Computer")]
        else:
            players = [Human("Player 1"), Human("Player 2")]
        return players[0], players[1]

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

    def play_one_round(self, first_player: Player, second_player: Player) -> None:
        """
        Runs a game of Tic Tac Toe between two players.

        Args:
            first_player: The first player in this round.
            second_player: The second player in this round.
        """
        # Display initial game board
        print(self.board)

        print(f"첫 번째 플레이어는 {first_player.name} (O)입니다.")
        print(f"두 번째 플레이어는 {second_player.name} (X)입니다.\n")

        # Cycle through players and their symbols
        symbol_player_pairs = cycle([("O", first_player), ("X", second_player)])
        for _ in range(len(self.board._current_state)):
            # Current player and corresponding symbol
            symbol, current_player = next(symbol_player_pairs)

            move = current_player.select_move(self.board.get_available_moves())
            self.board.apply_turn(move, symbol)

            # Display updated game board
            print(self.board)

            if self.board.is_finished():
                print(
                    f"{current_player.name}님 축하합니다!!! {current_player.name}님이 이겼습니다.\n"
                )
                current_player.wins += 1
                return

        # Board is full, draw game
        print("비겼습니다. 게임을 다시 시작해 보세요.\n")

    def run(self):
        """Executes the Tic Tac Toe Game."""
        # Initial welcome message
        print("#" * 60)
        print(f"{'Tic Tac Toe 게임에 오신 걸 환영합니다!':^50}")
        print("#" * 60, end="\n\n")
        print(f"{' Tic Tac Toe 게임을 시작합니다. ':*^52}\n")

        # Randomly select player order
        first_player, second_player = random.sample([self.player1, self.player2], k=2)

        while True:
            print(f'"Round {self.rounds_count}"\n')

            self.play_one_round(first_player, second_player)

            # Display current score
            print(f"| {f'{self.player1.name} vs. {self.player2.name}':^20} |")
            print(f"| {f'{self.player1.wins} 승':^9} {f'{self.player2.wins} 승':^9} |\n")

            if self.restart_game():
                # Prepare for next round: reset board and switch player order
                self.rounds_count += 1
                self.board.reset()
                first_player, second_player = second_player, first_player
            else:
                break

        # Goodbye message
        print(f"{' Tic Tac Toe 게임을 종료합니다. ':*^52}\n")
