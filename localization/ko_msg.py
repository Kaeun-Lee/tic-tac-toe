# localization/ko_msg.py
class KoMessage:
    def __init__(self, rounds_count: int) -> None:
        """
        Generates Korean game messages.

        Arg:
            rounds_count: The number of rounds played.
        """
        self.welcome = (
            f"{'#' * 60}\n\n{'Tic Tac Toe 게임에 오신 걸 환영합니다!':^50}\n\n{'#' * 60}\n"
        )
        self.start_game = f"{' Tic Tac Toe 게임을 시작합니다. ':*^52}\n"
        self.round = f'"{rounds_count} 라운드"\n'
        self.end_game = f"{' Tic Tac Toe 게임을 종료합니다. ':*^52}\n"
        self.draw_game = "비겼습니다. 게임을 다시 시작해 보세요.\n"
        self.replay_game = "게임을 다시 하시겠습니까? (y/n) : "
        self.invalid_yes_no = "잘못된 값을 입력했습니다. y/n 중 하나를 입력해 주세요.\n"
        self.invalid_position = "잘못된 값을 입력했습니다. 해당 칸의 번호를 입력해 주세요.\n"
        self.invalid_position_range = "이미 수가 놓인 위치를 선택했거나, 1 ~ 9 값을 넘어갔습니다."
        self.reselect_position = "위치를 다시 선택해 주세요.\n"

    def gets_players_intro(self, first_player: str, second_player: str) -> str:
        """
        Retrieves the introductory information for the players.

        Args:
            first_player: The name of the first player.
            second_player: The name of the second player.

        Return:
            players_intro: Intro info of current players.
        """
        players_intro = (
            f"첫 번째 플레이어는 {first_player} (O)입니다.\n두 번째 플레이어는 {second_player} (X)입니다.\n\n"
        )
        return players_intro

    def get_move_query(self, player_name: str) -> str:
        """
        Generates a move choice query.

        Arg:
            player_name: The name of the current player.

        Return:
            move_query: A prompt for player's move location.
        """
        move_query = f"{player_name}님, 놓을 위치를 선택해 주세요. : "
        return move_query

    def get_winner_msg(self, current_player: str) -> str:
        """
        Generates a winning message.

        Arg:
            current_player: The name of the winner.

        Return:
            winner_msg: A congratulatory message for the winner.
        """
        winner_msg = f"{current_player}님 축하합니다!!! {current_player}님이 이겼습니다.\n"
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
        scoreboard_msg = f"| {f'{player1_name} vs. {player2_name}':^20} |\n| {f'{player1_wins} 승':^9} {f'{player2_wins} 승':^9} |\n"
        return scoreboard_msg
