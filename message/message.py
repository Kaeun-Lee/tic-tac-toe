from abc import abstractmethod


class Message:
    def __init__(self) -> None:
        """Generates game messages."""
        self.start_game = self.get_start_game_message()
        self.end_game = self.get_end_game_message()
        self.draw_game = self.get_draw_game_message()
        self.replay_game = self.get_replay_game_message()
        self.invalid_yes_no = self.get_invalid_yes_no_message()
        self.invalid_position = self.get_invalid_position_message()
        self.invalid_position_range = self.get_invalid_position_range_message()
        self.reselect_position = self.get_reselect_position_message()

    @abstractmethod
    def get_start_game_message(self) -> str:
        """
        Generates the start game message.

        Return:
            Start game message.
        """
        ...

    @abstractmethod
    def get_end_game_message(self) -> str:
        """
        Generates the end game message.

        Return:
            End game message.
        """
        ...

    @abstractmethod
    def get_draw_game_message(self) -> str:
        """
        Generates the draw game message.

        Return:
            Draw game message.
        """
        ...

    @abstractmethod
    def get_replay_game_message(self) -> str:
        """
        Generates a replay query message.

        Return:
            Prompt for replay.
        """
        ...

    @abstractmethod
    def get_invalid_yes_no_message(self) -> str:
        """
        Generates an error message for invalid 'yes' or 'no' responses.

        Return:
            Error message for invalid responses.
        """
        ...

    @abstractmethod
    def get_invalid_position_message(self) -> str:
        """
        Generates an error message for invalid position input.

        Return:
            Error message for invalid position.
        """
        ...

    @abstractmethod
    def get_invalid_position_range_message(self) -> str:
        """
        Generates an error message for out-of-range position input.

        Return:
            Error message for out-of-range position.
        """
        ...

    @abstractmethod
    def get_reselect_position_message(self) -> str:
        """
        Generates a message to reselect position.

        Return:
            Position reselection message.
        """
        ...

    @abstractmethod
    def get_round_count(self, round: int) -> str:
        """
        Generates a round count message.

        Arg:
            round: Current round number.

        Return:
            Current round number message.
        """
        ...

    @abstractmethod
    def get_players_intro(self, first_player: str, second_player: str) -> str:
        """
        Generates the introductory information message for the players.

        Args:
            first_player: Name of the first player.
            second_player: Name of the second player.

        Return:
            Introductory message for the current players.
        """
        ...

    @abstractmethod
    def get_move_query(self, player_name: str) -> str:
        """
        Generates move query for current player.

        Arg:
            player_name: Name of the current player.

        Return:
            Prompt for player's move location.
        """
        ...

    @abstractmethod
    def get_winner_message(self, winner_name: str) -> str:
        """
        Generates a winning message.

        Arg:
            winner_name: Name of the winner.

        Return:
            Congratulatory message for the winner.
        """
        ...

    @abstractmethod
    def get_scoreboard_message(
        self, player1_name: str, player2_name: str, player1_wins: int, player2_wins: int
    ) -> str:
        """
        Generates a game score message.

        Args:
            player1_name: Name of one player.
            player2_name: Name of the other player.
            player1_wins: Number of wins for the player1.
            player2_wins: Number of wins for the player2.

        Return:
            Current game score message.
        """
        ...
