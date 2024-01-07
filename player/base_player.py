class Player:
    def __init__(self, name):
        """A player choosing from available game moves."""
        self.name = name
        self.wins = 0

    def select_move(self, available_moves: list[int]) -> int:
        """
        Selects a move from the available options.

        Arg:
            available_moves: Unoccupied positions in the current game state.

        Return:
            The selected move.
        """
        ...
