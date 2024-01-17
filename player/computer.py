import random
import time

from message import Message
from .player import Player


class Computer(Player):
    """Computer player in the game."""

    def select_move(self, available_moves: list[int], message: Message) -> int:
        """
        Randomly selects a move from the available options.

        Args:
            available_moves: Unoccupied positions in the current game state.
            message: Message object for generating game messages.

        Return:
            selected_move: Randomly selected position.
        """
        print(message.current_language.get_move_query(self.name))
        print()

        time.sleep(1)
        selected_move = random.choice(available_moves)
        return selected_move
