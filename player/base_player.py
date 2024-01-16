from localization import MessageFactory


class Player:
    def __init__(self, name):
        """A player choosing from available game moves."""
        self.name = name
        self.wins = 0

    def select_move(
        self, available_moves: list[int], msg_factory: MessageFactory
    ) -> int:
        """
        Selects a move from the available options.

        Args:
            available_moves: Unoccupied positions in the current game state.
            msg_factory: A MessageFactory object for generating game messages.

        Return:
            The selected move.
        """
        ...
