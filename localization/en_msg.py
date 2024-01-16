# localization/en_msg.py
class EnMessage:
    def __init__(self, rounds_count: int) -> None:
        """
        Generates English game messages.

        Arg:
            rounds_count: The number of rounds played.
        """
        self.welcome = (
            f"{'#' * 60}\n\n{'Welcome to the Tic Tac Toe game!':^60}\n\n{'#' * 60}\n"
        )
        self.start_game = f"{' The Tic Tac Toe game is starting. ':*^60}\n"
        self.round = f'"Round {rounds_count}"\n'
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

    def gets_players_intro(self, first_player: str, second_player: str) -> str:
        """
        Retrieves the introductory information for the players.

        Args:
            first_player: The name of the first player.
            second_player: The name of the second player.

        Return:
            players_intro: Intro info of current players.
        """
        players_intro = f"The first player is {first_player} (O).\nThe second player is {second_player} (X).\n"
        return players_intro

    def get_move_query(self, player_name: str) -> str:
        """
        Creates move query for current player.

        Arg:
            player_name: The name of the current player.

        Return:
            move_query: A prompt for player's move location.
        """
        move_query = f"{player_name}, please select a position to place your move. : "
        return move_query

    def get_winner_msg(self, current_player: str) -> str:
        """
        Generates a winning message.

        Arg:
            current_player: The name of the winner.

        Return:
            winner_msg: A congratulatory message for the winner.
        """
        winner_msg = (
            f"Congratulations, {current_player}!!! {current_player}, you have won.\n"
        )
        return winner_msg

    def get_scoreboard_msg(
        self, player1_name: str, player2_name: str, player1_wins: int, player2_wins: int
    ) -> str:
        """
        Generates a game score message.

        Args:
            player1_name: The name of one player.
            player2_name: The name of the other player.
            player1_wins: The number of wins for the player1.
            player2_wins: The number of wins for the player2.

        Return:
            scoreboard_msg: The current game score message.
        """
        scoreboard_msg = f"| {f'{player1_name} vs. {player2_name}':^20} |\n| {f'{player1_wins} win':^9} {f'{player2_wins} win':^9} |\n"
        return scoreboard_msg
