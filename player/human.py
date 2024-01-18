from message import English, Korean

from .player import Player


class Human(Player):
    """Human player in the game."""

    def select_move(self, available_moves: list[int], message: English | Korean) -> int:
        """
        Prompts the user to select a move from the available options.

        Args:
            available_moves: Unoccupied positions in the current game state.
            message: Object storing game messages.

        Return:
            selected_move: User-selected position.
        """
        while True:
            try:
                # Get user input
                selected_move = int(input(message.get_move_query(self.name)))
                print()
            except ValueError:
                # Non-integer input
                print(message.invalid_position)
            else:
                # Check if valid move
                if selected_move in available_moves:
                    return selected_move
                else:
                    print(message.invalid_position_range)
                    print(message.reselect_position)
