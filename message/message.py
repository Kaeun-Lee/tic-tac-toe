from message import language_dict


class Message:
    """Generates game messages."""

    def __init__(self, language) -> None:
        self.start_border_length = 60

        if language == "en":
            self.language_settings = language_dict.english
            self.welcome_message_formatting_width = 60
            self.start_message_formatting_width = 60
            self.end_message_formatting_width = 60
            self.scoreboard_name_formatting_width = 20
            self.scoreboard_player1_formatting_width = 10
            self.scoreboard_player2_formatting_width = 10
        else:
            self.language_settings = language_dict.korean
            self.welcome_message_formatting_width = 50
            self.start_message_formatting_width = 52
            self.end_message_formatting_width = 52
            self.scoreboard_name_formatting_width = 20
            self.scoreboard_player1_formatting_width = 9
            self.scoreboard_player2_formatting_width = 9

    def get_start_game_message(self) -> str:
        """
        Generates the start game message at the beginning of the game.

        Return:
            Message that indicates the start of the game.
        """
        border_line = "#" * self.start_border_length
        welcome_message = self.language_settings["welcome message"].center(
            self.welcome_message_formatting_width
        )
        start_message = self.language_settings["start message"].center(
            self.start_message_formatting_width
        )

        return (
            f"{border_line}\n\n{welcome_message}\n\n{border_line}\n\n{start_message}\n"
        )

    def get_end_game_message(self) -> str:
        """
        Generates the end game message at the end of the game.

        Return:
            Message that indicates the end of the game.
        """
        end_message = self.language_settings["end message"].center(
            self.end_message_formatting_width, "*"
        )
        return f"{end_message}\n"

    def get_draw_game_message(self) -> str:
        """
        Generates the draw game message when all positions on the board are filled and no player has won.

        Return:
            Message that informs players of the draw and suggests a new game.
        """
        return self.language_settings["draw message"]

    def get_round_count(self, round: int) -> str:
        """
        Generates a message displaying the current round number.

        Informs users about the current round at the beginning of each round.

        Arg:
            round: Current round number.

        Return:
            Message that indicates the current round number.
        """
        return self.language_settings["round count message"].format(round)

    def get_players_intro(self, first_player: str, second_player: str) -> str:
        """
        Generates the introductory information message for the players at the beginning of the game.

        Args:
            first_player: Name of the first player.
            second_player: Name of the second player.

        Return:
            Message that introduces the first and second player.
        """
        players = {"first_player": first_player, "second_player": second_player}
        return self.language_settings["players intro message"].format(**players)

    def get_move_query(self, player_name: str) -> str:
        """
        Generates move query when it's the player's turn.

        Arg:
            player_name: Name of the current player.

        Return:
            Message that asks for the player's move location.
        """
        return self.language_settings["move query message"].format(player_name)

    def get_winner_message(self, winner_name: str) -> str:
        """
        Generates a winning message when a player has won the game.

        Arg:
            winner_name: Name of the winner.

        Return:
            Message that congratulates the winner.
        """
        return self.language_settings["winner message"].format(winner_name)

    def get_scoreboard_message(
        self, player1_name: str, player2_name: str, player1_wins: int, player2_wins: int
    ) -> str:
        """
        Generates a game score message after each round to inform of the current score.

        Args:
            player1_name: Name of one player.
            player2_name: Name of the other player.
            player1_wins: Number of wins for the player1.
            player2_wins: Number of wins for the player2.

        Return:
            Message that displays the current game score.
        """
        name = f"{player1_name} vs. {player2_name}".center(
            self.scoreboard_name_formatting_width
        )
        player1 = (
            f"{player1_wins} {self.language_settings['scoreboard message']}".center(
                self.scoreboard_player1_formatting_width
            )
        )
        player2 = (
            f"{player2_wins} {self.language_settings['scoreboard message']}".center(
                self.scoreboard_player2_formatting_width
            )
        )
        return f"| {name} |\n| {player1} {player2} |\n"

    def get_replay_game_message(self) -> str:
        """
        Generates a replay query message when one round is over.

        Will ask yes or no question if the user wants to play another round.

        Return:
            Message that requests a decision on replay.
        """
        return self.language_settings["replay message"]

    def get_invalid_yes_no_message(self) -> str:
        """
        Generates an error message for invalid 'yes' or 'no' responses.

        Informs the user they have provided an invalid input when a 'yes' or 'no' response was expected.

        Return:
            Error message for invalid 'yes' or 'no' inputs.
        """
        return self.language_settings["invalid yes or no message"]

    def get_invalid_position_message(self) -> str:
        """
        Generates an error message for an invalid position input.

        Informs the user that the input they have provided does not correspond to a valid position on the game board.

        Return:
            Error message for invalid position input.
        """
        return self.language_settings["invalid position message"]

    def get_invalid_position_range_message(self) -> str:
        """
        Generates an error message when a position input is out of the valid range.

        Return:
            Error message for a position that is out of range.
        """
        return self.language_settings["invalid position range message"]

    def get_reselect_position_message(self) -> str:
        """
        Generates a message to reselect position.

        Return:
            Message that asks for position reselection.
        """
        return self.language_settings["reselect position message"]
