from message import Message

from .player import Player


class Human(Player):
    """Human player in the game."""

    def select_move(self, available_moves: list[int], message: Message) -> int:
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
                print(message.get_invalid_position_message())
            else:
                # Check if valid move
                if selected_move in available_moves:
                    return selected_move
                else:
                    print(message.get_invalid_position_range_message())
                    print(message.get_reselect_position_message())
