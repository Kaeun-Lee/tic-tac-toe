import random
import time

from .base_player import Player


class Computer(Player):
    """A Computer player in the game."""

    def select_move(self, available_moves: list[int], language: str) -> int:
        """
        Randomly selects a move from the available options.

        Args:
            available_moves: Unoccupied positions in the current game state.
            language: The language code for the game messages (e.g., 'en', 'ko').

        Return:
            selected_move: The randomly selected position.
        """
        time.sleep(0.8)
        selected_move = random.choice(available_moves)
        return selected_move
