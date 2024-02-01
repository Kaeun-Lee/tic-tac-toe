from .message import Message


class English(Message):
    """Generates English game messages."""

    def get_start_game_message(self) -> str:
        return f"{'#' * 60}\n\n{'Welcome to the Tic Tac Toe game!':^60}\n\n{'#' * 60}\n\n{' The Tic Tac Toe game is starting. ':*^60}\n"

    def get_end_game_message(self) -> str:
        return f"{' The Tic Tac Toe game is ending. ':*^52}\n"

    def get_draw_game_message(self) -> str:
        return "It's a draw. Please try the game again.\n"

    def get_replay_game_message(self) -> str:
        return "Do you want to play the game again? (y/n) : "

    def get_invalid_yes_no_message(self) -> str:
        return "You've entered an invalid value. Please enter either y or n.\n"

    def get_invalid_position_message(self) -> str:
        return "Invalid value. Please enter the number of the desired position.\n"

    def get_invalid_position_range_message(self) -> str:
        return "You've selected a position that's already taken or exceeded the value of 1 ~ 9."

    def get_reselect_position_message(self) -> str:
        return "Please select the position again.\n"

    def get_round_count(self, round: int) -> str:
        return f'"Round {round}"\n'

    def get_players_intro(self, first_player: str, second_player: str) -> str:
        return f"The first player is {first_player} (O).\nThe second player is {second_player} (X).\n"

    def get_move_query(self, player_name: str) -> str:
        return f"{player_name}, please select a position to place your move. : "

    def get_winner_message(self, winner_name: str) -> str:
        return f"Congratulations, {winner_name}!!! {winner_name}, you have won.\n"

    def get_scoreboard_message(
        self, player1_name: str, player2_name: str, player1_wins: int, player2_wins: int
    ) -> str:
        return f"| {f'{player1_name} vs. {player2_name}':^20} |\n| {f'{player1_wins} win':^10} {f'{player2_wins} win':^10} |\n"
