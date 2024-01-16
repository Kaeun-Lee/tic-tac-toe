from localization import MessageFactory

from .base_player import Player


class Human(Player):
    """A Human player in the game."""

    def select_move(
        self, available_moves: list[int], msg_factory: MessageFactory
    ) -> int:
        """
        Prompts the user to select a move from the available options.

        Args:
            available_moves: Unoccupied positions in the current game state.
            msg_factory: A MessageFactory object for generating game messages.

        Return:
            selected_move: The user-selected position.
        """
        while True:
            try:
                # Get user input
                selected_move = int(
                    input(msg_factory.current_language.get_move_query(self.name))
                )
                print()
            except ValueError:
                # Non-integer input
                print(msg_factory.current_language.invalid_position)
            else:
                # Check if valid move
                if selected_move in available_moves:
                    return selected_move
                else:
                    print(msg_factory.current_language.invalid_position_range)
                    print(msg_factory.current_language.reselect_position)
