class Player:
    """A player choosing from available game moves."""

    def __init__(self, name):
        self.name = name

    def select_move(self, available_moves: set[int]) -> int:
        """
        Select a move from the available options.

        Args:
            available_moves: A set of integers for usable game moves.

        Returns:
            int: The selected move.
        """
        ...
