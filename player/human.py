from .base_player import Player


class Human(Player):
    """A Human player in the game."""

    def select_move(self, available_moves: list[int], language: str) -> int:
        """
        Prompts the user to select a move from the available options.

        Args:
            available_moves: Unoccupied positions in the current game state.
            language: The language code for the game messages (e.g., 'en', 'ko').

        Return:
            selected_move: The user-selected position.
        """
        while True:
            try:
                # Get user input
                if language == "en":
                    selected_move = int(
                        input(
                            f"{self.name}, please select a position to place your move. : "
                        )
                    )
                else:
                    selected_move = int(input(f"{self.name}님, 놓을 위치를 선택해 주세요. : "))

                print()
            except ValueError:
                # Non-integer input
                if language == "en":
                    print(
                        "Invalid value. Please enter the number of the desired position.\n"
                    )
                else:
                    print("잘못된 값을 입력했습니다. 해당 칸의 번호를 입력해 주세요.\n")
            else:
                # Check if valid move
                if selected_move in available_moves:
                    return selected_move
                else:
                    if language == "en":
                        print(
                            "You've selected a position that's already taken or exceeded the value of 1 ~ 9."
                        )
                        print("Please select the position again.\n")
                    else:
                        print("이미 수가 놓인 위치를 선택했거나, 1 ~ 9 값을 넘어갔습니다.")
                        print("위치를 다시 선택해 주세요.\n")
