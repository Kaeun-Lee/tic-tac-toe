# game.py
import random
from itertools import cycle

from board import Board
from localization import MessageFactory
from player import Computer, Human, Player


class TicTacToeGame:
    def __init__(self, num_players: int, language: str) -> None:
        """
        Represents a game of Tic Tac Toe.

        Args:
            num_players: The number of players chosen by the user.
            language: The language code for the game messages (e.g., 'en', 'ko').O
        """
        self.player1, self.player2 = self.set_players(num_players)
        self.rounds_count = 1
        self.board = Board()
        self.msg_factory = MessageFactory(language, self.rounds_count)

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
            play_again = input(self.msg_factory.current_language.replay_game)
            print()
            if play_again in ["y", "n"]:
                break
            else:
                print(self.msg_factory.current_language.invalid_yes_no)
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

        print(
            self.msg_factory.current_language.gets_players_intro(
                first_player.name, second_player.name
            )
        )

        # Cycle through players and their symbols
        symbol_player_pairs = cycle([("O", first_player), ("X", second_player)])
        for _ in range(len(self.board._current_state)):
            # Current player and corresponding symbol
            symbol, current_player = next(symbol_player_pairs)

            move = current_player.select_move(
                self.board.get_available_moves(),
                self.msg_factory,
            )
            self.board.apply_turn(move, symbol)

            # Display updated game board
            print(self.board)

            if self.board.is_finished():
                print(
                    self.msg_factory.current_language.get_winner_msg(
                        current_player.name
                    )
                )
                current_player.wins += 1
                return

        # Board is full, draw game
        print(self.msg_factory.current_language.draw_game)

    def run(self) -> None:
        """Executes the Tic Tac Toe Game."""
        # Initial welcome message
        print(self.msg_factory.current_language.welcome)
        print(self.msg_factory.current_language.start_game)

        # Randomly select player order
        first_player, second_player = random.sample([self.player1, self.player2], k=2)

        while True:
            print(self.msg_factory.current_language.round)

            self.play_one_round(first_player, second_player)

            # Display current score
            print(
                self.msg_factory.current_language.get_scoreboard_msg(
                    self.player1.name,
                    self.player2.name,
                    self.player1.wins,
                    self.player2.wins,
                )
            )

            if self.restart_game():
                # Prepare for next round: reset board and switch player order
                self.rounds_count += 1
                self.board.reset()
                first_player, second_player = second_player, first_player
            else:
                break

        # Goodbye message
        print(self.msg_factory.current_language.end_game)
