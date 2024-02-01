from abc import ABC, abstractmethod


class Message(ABC):
    """Generates game messages."""

    @abstractmethod
    def get_start_game_message(self) -> str:
        """
        Generates the start game message at the beginning of the game.

        Return:
            Message that indicates the start of the game.
        """
        ...

    @abstractmethod
    def get_end_game_message(self) -> str:
        """
        Generates the end game message at the end of the game.

        Return:
            Message that indicates the end of the game.
        """
        ...

    @abstractmethod
    def get_draw_game_message(self) -> str:
        """
        Generates the draw game message when all positions on the board are filled and no player has won.

        Return:
            Message that informs players of the draw and suggests a new game.
        """
        ...

    @abstractmethod
    def get_replay_game_message(self) -> str:
        """
        Generates a replay query message when one round is over.

        Will ask yes or no question if the user wants to play another round.

        Return:
            Message that requests a decision on replay.
        """
        ...

    @abstractmethod
    def get_invalid_yes_no_message(self) -> str:
        """
        Generates an error message for invalid 'yes' or 'no' responses.

        Informs the user they have provided an invalid input when a 'yes' or 'no' response was expected.

        Return:
            Error message for invalid 'yes' or 'no' inputs.
        """
        ...

    @abstractmethod
    def get_invalid_position_message(self) -> str:
        """
        Generates an error message for an invalid position input.

        Informs the user that the input they have provided does not correspond to a valid position on the game board.

        Return:
            Error message for invalid position input.
        """
        ...

    @abstractmethod
    def get_invalid_position_range_message(self) -> str:
        """
        Generates an error message when a position input is out of the valid range.

        Return:
            Error message for a position that is out of range.
        """
        ...

    @abstractmethod
    def get_reselect_position_message(self) -> str:
        """
        Generates a message to reselect position.

        Return:
            Message that asks for position reselection.
        """
        ...

    @abstractmethod
    def get_round_count(self, round: int) -> str:
        """
        Generates a message displaying the current round number.

        Informs users about the current round at the beginning of each round.

        Arg:
            round: Current round number.

        Return:
            Message that indicates the current round number.
        """
        ...

    @abstractmethod
    def get_players_intro(self, first_player: str, second_player: str) -> str:
        """
        Generates the introductory information message for the players at the beginning of the game.

        Args:
            first_player: Name of the first player.
            second_player: Name of the second player.

        Return:
            Message that introduces the first and second player.
        """
        ...

    @abstractmethod
    def get_move_query(self, player_name: str) -> str:
        """
        Generates move query when it's the player's turn.

        Arg:
            player_name: Name of the current player.

        Return:
            Message that asks for the player's move location.
        """
        ...

    @abstractmethod
    def get_winner_message(self, winner_name: str) -> str:
        """
        Generates a winning message when a player has won the game.

        Arg:
            winner_name: Name of the winner.

        Return:
            Message that congratulates the winner.
        """
        ...

    @abstractmethod
    def get_scoreboard_message(
        self, player1_name: str, player2_name: str, player1_wins: int, player2_wins: int
    ) -> str:
        """
        Generates a game score message after each round to inform players about the current score.

        Args:
            player1_name: Name of one player.
            player2_name: Name of the other player.
            player1_wins: Number of wins for the player1.
            player2_wins: Number of wins for the player2.

        Return:
            Message that displays the current game score.
        """
        ...
