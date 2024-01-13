class Player:
    def __init__(self, name):
        """A player choosing from available game moves."""
        self.name = name
        self.wins = 0

    def select_move(self, available_moves: list[int], language: str) -> int:
        """
        Selects a move from the available options.

        Args:
            available_moves: Unoccupied positions in the current game state.
            language: The language code for the game messages (e.g., 'en', 'ko').

        Return:
            The selected move.
        """
        ...
