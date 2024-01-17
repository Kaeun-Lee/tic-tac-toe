from message import Message


class Player:
    def __init__(self, name):
        """A player choosing from available game moves."""
        self.name = name
        self.wins = 0

    def select_move(self, available_moves: list[int], message: Message) -> int:
        """
        Selects a move from the available options.

        Args:
            available_moves: Unoccupied positions in the current game state.
            message: Message object for generating game messages.

        Return:
            selected move.
        """
        ...
