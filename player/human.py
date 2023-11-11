from .base_player import Player


class Human(Player):
    """A Human player in the game."""

    def select_move(self, available_moves: set[int]) -> int:
        """
        Prompt the user to select a move from the available options.

        Note: The function modifies 'available_moves'.

        Args:
            available_moves: A set of integers for usable game moves.

        Returns:
            selected_move : The selected move.
        """
        while True:
            try:
                # get user input
                selected_move = int(input(f"{self.name}님, 놓을 위치를 선택해 주세요 : "))
            except ValueError:
                # non-integer input
                print("잘못된 값을 입력했습니다. 위치를 정수로 입력해 주세요.\n")
            else:
                # check if valid move
                if selected_move in available_moves:
                    # remove chosen move from options
                    available_moves.remove(selected_move)

                    return selected_move
                else:
                    print("이미 수가 놓인 위치를 선택했거나, 1 ~ 9 값을 넘어갔습니다.")
                    print("위치를 다시 선택해 주세요.\n")
