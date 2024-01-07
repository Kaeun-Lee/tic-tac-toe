import numpy as np


class Board:
    def __init__(self) -> None:
        """A Tic Tac Toe game board with methods for game progress and status check."""

        self._current_state = np.array(range(1, 10), dtype=object)

        # Winning patterns
        self._victory_rules: list[list[int]] = [
            [0, 1, 2],
            [3, 4, 5],
            [6, 7, 8],
            [0, 3, 6],
            [1, 4, 7],
            [2, 5, 8],
            [0, 4, 8],
            [2, 4, 6],
        ]

    def __str__(self) -> str:
        """
        Formats the game board into a displayable string.

        Return:
            current_state: A string representation of the game board.
        """
        current_state = "\n".join(
            f"{' | '.join(map(str, self._current_state[i : i + 3])):^24}"
            for i in range(0, len(self._current_state), 3)
        )
        return f"<Tic Tac Toe Game Board>\n\n{current_state}\n\n"

    def reset(self) -> None:
        """Initializes the game board for a new round."""
        self._current_state = np.array(range(1, 10), dtype=object)

    def get_available_moves(self) -> list[int]:
        """
        Gets permissible moves in the current state.

        Return:
            available_moves: Unoccupied positions in the current game state.
        """
        available_moves = [
            move for move in self._current_state if isinstance(move, int)
        ]
        return available_moves

    def all_elements_equal(self, rule: list[int]) -> bool:
        """
        Checks if all elements at given indices are identical.

        Arg:
            rule: Indices to be checked.

        Return:
            True if elements at given indices are the same, False otherwise.
        """
        return all(self._current_state[rule] == self._current_state[rule[0]])

    def is_finished(self) -> bool:
        """
        Checks for game end.

        Return:
            True if the game is finished (i.e., resulted in a win), False otherwise.
        """
        for rule in self._victory_rules:
            if self.all_elements_equal(rule):
                return True
        return False

    def apply_turn(self, move: int, symbol: str) -> None:
        """
        Apply a player's move to the board.

        Args:
            move: The board position that was just selected (1 ~ 9).
            symbol: The symbol that was just played ('O' or 'X').
        """
        self._current_state[move - 1] = symbol
