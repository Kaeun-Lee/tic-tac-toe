from message import English, Korean


class Player:
    def __init__(self, name):
        """A player choosing from available game moves."""
        self.name = name
        self.wins = 0

    def select_move(self, available_moves: list[int], message: English | Korean) -> int:
        """
        Selects a move from the available options.

        Args:
            available_moves: Unoccupied positions in the current game state.
            message: Object storing game messages.

        Return:
            selected move.
        """
        ...
