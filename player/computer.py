import random
import time

from localization import MessageFactory

from .base_player import Player


class Computer(Player):
    """A Computer player in the game."""

    def select_move(
        self, available_moves: list[int], msg_factory: MessageFactory
    ) -> int:
        """
        Randomly selects a move from the available options.

        Args:
            available_moves: Unoccupied positions in the current game state.
            msg_factory: A MessageFactory object for generating game messages.

        Return:
            selected_move: The randomly selected position.
        """
        print(msg_factory.current_language.get_move_query(self.name))
        print()

        time.sleep(1)
        selected_move = random.choice(available_moves)
        return selected_move
