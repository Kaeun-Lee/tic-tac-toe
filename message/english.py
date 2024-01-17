class English:
    def __init__(self) -> None:
        """Generates English game messages."""
        self.start_game = f"{'#' * 60}\n\n{'Welcome to the Tic Tac Toe game!':^60}\n\n{'#' * 60}\n\n{' The Tic Tac Toe game is starting. ':*^60}\n"

        self.end_game = f"{' The Tic Tac Toe game is ending. ':*^52}\n"
        self.draw_game = "It's a draw. Please try the game again.\n"
        self.replay_game = "Do you want to play the game again? (y/n) : "
        self.invalid_yes_no = (
            "You've entered an invalid value. Please enter either y or n.\n"
        )

        self.invalid_position = (
            "Invalid value. Please enter the number of the desired position.\n"
        )
        self.invalid_position_range = "You've selected a position that's already taken or exceeded the value of 1 ~ 9."
        self.reselect_position = "Please select the position again.\n"

    def get_round_count(self, round: int) -> str:
        """
        Generates a round count message.

        Arg:
            round: Current round number.

        Return:
            Current round number message.
        """
        return f'"Round {round}"\n'

    def get_players_intro(self, first_player: str, second_player: str) -> str:
        """
        Retrieves the introductory information for the players.

        Args:
            first_player: Name of the first player.
            second_player: Name of the second player.

        Return:
            Intro info of current players.
        """
        return f"The first player is {first_player} (O).\nThe second player is {second_player} (X).\n"

    def get_move_query(self, player_name: str) -> str:
        """
        Generates move query for current player.

        Arg:
            player_name: Name of the current player.

        Return:
            Prompt for player's move location.
        """
        return f"{player_name}, please select a position to place your move. : "

    def get_winner_message(self, winner_name: str) -> str:
        """
        Generates a winning message.

        Arg:
            winner_name: Name of the winner.

        Return:
            Congratulatory message for the winner.
        """
        return f"Congratulations, {winner_name}!!! {winner_name}, you have won.\n"

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
        return f"| {f'{player1_name} vs. {player2_name}':^20} |\n| {f'{player1_wins} win':^10} {f'{player2_wins} win':^10} |\n"
