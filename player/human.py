from message import Message

from .player import Player


class Human(Player):
    """Human player in the game."""

    def select_move(self, available_moves: list[int], message: Message) -> int:
        """
        Prompts the user to select a move from the available options.

        Args:
            available_moves: Unoccupied positions in the current game state.
            message: Message object for generating game messages.

        Return:
            selected_move: User-selected position.
        """
        while True:
            try:
                # Get user input
                selected_move = int(
                    input(message.current_language.get_move_query(self.name))
                )
                print()
            except ValueError:
                # Non-integer input
                print(message.current_language.invalid_position)
            else:
                # Check if valid move
                if selected_move in available_moves:
                    return selected_move
                else:
                    print(message.current_language.invalid_position_range)
                    print(message.current_language.reselect_position)
