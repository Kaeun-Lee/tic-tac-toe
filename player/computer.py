import random

from .base_player import Player


class Computer(Player):
    """A Computer player in the game."""

    def select_move(self, available_moves: set[int]) -> int:
        """
        Randomly select a move from the available options.

        Note: The function modifies 'available_moves'.

        Args:
            available_moves: A set of integers for usable game moves.

        Returns:
            selected_move : The selected move.
        """
        # select random move
        selected_move = random.choice(list(available_moves))

        # remove chosen move from options
        available_moves.remove(selected_move)

        return selected_move
