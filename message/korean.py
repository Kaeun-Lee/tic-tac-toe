from .message import Message


class Korean(Message):
    """Generates Korean game messages."""

    def get_start_game_message(self) -> str:
        return f"{'#' * 60}\n\n{'Tic Tac Toe 게임에 오신 걸 환영합니다!':^50}\n\n{'#' * 60}\n\n{' Tic Tac Toe 게임을 시작합니다. ':*^52}\n"

    def get_end_game_message(self) -> str:
        return f"{' Tic Tac Toe 게임을 종료합니다. ':*^52}\n"

    def get_draw_game_message(self) -> str:
        return "비겼습니다. 게임을 다시 시작해 보세요.\n"

    def get_replay_game_message(self) -> str:
        return "게임을 다시 하시겠습니까? (y/n) : "

    def get_invalid_yes_no_message(self) -> str:
        return "잘못된 값을 입력했습니다. y/n 중 하나를 입력해 주세요.\n"

    def get_invalid_position_message(self) -> str:
        return "잘못된 값을 입력했습니다. 해당 칸의 번호를 입력해 주세요.\n"

    def get_invalid_position_range_message(self) -> str:
        return "이미 수가 놓인 위치를 선택했거나, 1 ~ 9 값을 넘어갔습니다."

    def get_reselect_position_message(self) -> str:
        return "위치를 다시 선택해 주세요.\n"

    def get_round_count(self, round: int) -> str:
        return f'"{round} 라운드"\n'

    def get_players_intro(self, first_player: str, second_player: str) -> str:
        return (
            f"첫 번째 플레이어는 {first_player} (O)입니다.\n두 번째 플레이어는 {second_player} (X)입니다.\n\n"
        )

    def get_move_query(self, player_name: str) -> str:
        return f"{player_name}님, 놓을 위치를 선택해 주세요. : "

    def get_winner_message(self, winner_name: str) -> str:
        return f"{winner_name}님 축하합니다!!! {winner_name}님이 이겼습니다.\n"

    def get_scoreboard_message(
        self, player1_name: str, player2_name: str, player1_wins: int, player2_wins: int
    ) -> str:
        return f"| {f'{player1_name} vs. {player2_name}':^20} |\n| {f'{player1_wins} 승':^9} {f'{player2_wins} 승':^9} |\n"
