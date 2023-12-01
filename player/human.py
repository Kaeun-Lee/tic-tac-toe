from .base_player import Player


class Human(Player):
    """A Human player in the game."""

    def select_move(self, available_moves: list[int]) -> int:
        """
        Prompts the user to select a move from the available options.

        Arg:
            available_moves: Unoccupied positions in the current game state.

        Return:
            selected_move: The user-selected position.
        """
        while True:
            try:
                # Get user input
                selected_move = int(input(f"{self.name}님, 놓을 위치를 선택해 주세요 : "))
                print()
            except ValueError:
                # Non-integer input
                print("잘못된 값을 입력했습니다. 위치를 정수로 입력해 주세요.\n")
            else:
                # Check if valid move
                if selected_move in available_moves:
                    return selected_move
                else:
                    print("이미 수가 놓인 위치를 선택했거나, 1 ~ 9 값을 넘어갔습니다.")
                    print("위치를 다시 선택해 주세요.\n")
