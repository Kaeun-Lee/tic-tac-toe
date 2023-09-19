import random
from collections import deque

print("#" * 60)
print(f"{'Tic Tac Toe 게임에 오신 걸 환영합니다!':^50}")
print("#" * 60)

print(
    """
게임 방식을 선택해 주세요.
(1) 1 PLAYER
(2) 2 PLAYER\n"""
)

print("첫 번째 플레이어는 computer (O)입니다.")
print("두 번째 플레이어는 player1 (X)입니다.\n")
print()

print(f"{' Tic Tac Toe 게임을 시작합니다. ':*^52}\n")

game_board = []
position = 1

for _ in range(3):
    game_board.append([str(position + j) for j in range(3)])
    position += 3


def print_game_board():
    """Print the current state of the game board."""
    print("<Tic Tac Toe Game Board>")
    for board_row in game_board:
        for j in board_row:
            print(j, end=" ")
        print()
    print()


print_game_board()


game_board_position = {
    1: (0, 0),
    2: (0, 1),
    3: (0, 2),
    4: (1, 0),
    5: (1, 1),
    6: (1, 2),
    7: (2, 0),
    8: (2, 1),
    9: (2, 2),
}

symbols = {"O": 0, "X": -1}
computer_symbol = "O"
player1_symbol = "X"

board_position = deque([1, 2, 3, 4, 5, 6, 7, 8, 9])
random.shuffle(board_position)

victory_rules = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9],
    [1, 5, 9],
    [3, 5, 7],
]


def is_finished(symbol: str, move: int) -> bool:
    """
    Check if the game has ended based on the latest move.

    Args:
        symbol: The symbol that was just played. ('O' or 'X')
        move: The position that was just selected. (1 ~ 9)

    Returns:
        bool: True if the game is finished (i.e., resulted in a win), otherwise False
    """
    for rule in victory_rules:
        if move in rule:
            rule[rule.index(move)] = symbols[symbol]
        # current player's win, game over
        if rule.count(symbols[symbol]) == 3:
            return True
    return False


def execute_computer_turn(player: str, symbol: str) -> bool:
    """
    Executes a turn for computer.

    Args:
        player: The name of the player. (in this case 'computer')
        symbol: The symbol that represents this player on the game board. ('O' or 'X')

    Returns:
        bool: True if the move has finished the game (i.e., resulted in a win), otherwise False
    """
    print(f"{player}님 ({symbol})을 놓을 위치를 선택해 주세요.")

    move = board_position.popleft()
    print(f"{player}님이 선택한 위치는 {move}입니다.\n")

    x, y = game_board_position[move]
    game_board[x][y] = symbol

    # check game over
    return is_finished(symbol, move)


def execute_player1_turn(player: str, symbol: str) -> bool:
    """
    Executes a turn for player1.

    Args:
        player: The name of the player. (in this case 'player1')
        symbol: The symbol that represents this player on the game board. ('O' or 'X')

    Returns:
        bool: True if the move has finished the game (i.e., resulted in a win), otherwise False
    """
    while True:
        try:
            move = int(input(f"{player}님 ({symbol})을 놓을 위치를 선택해 주세요 : "))
        except ValueError:
            # handle non-integer input
            print("잘못된 값을 입력했습니다. 위치를 정수로 입력해 주세요.\n")
        else:
            # confirm player's choice
            if move in board_position and move in range(1, 10):
                print(f"{player}님이 선택한 위치는 {move}입니다.\n")

                x, y = game_board_position[move]
                game_board[x][y] = symbol

                # prevent duplicate moves
                board_position.remove(move)

                # check game over
                return is_finished(symbol, move)

            else:
                print("이미 수가 놓인 위치를 선택했거나, 1 ~ 9 값을 넘어갔습니다.")
                print("위치를 다시 선택해 주세요.\n")


def play_game() -> None:
    """Run a game between a computer and a player."""
    while True:
        if board_position and execute_computer_turn("computer", computer_symbol):
            # computer win
            print_game_board()
            print("축하합니다!!! computer님이 이겼습니다.")
            break

        # computer does not win. print gameboard for player1's reference.
        print_game_board()

        if board_position and execute_player1_turn("player1", player1_symbol):
            # player1 win
            print_game_board()
            print("축하합니다!!! player1님이 이겼습니다.")
            break

        # player1 does not win. print gameboard for computer's reference.
        print_game_board()

        if not board_position:
            # board is full, draw
            print("비겼습니다. 게임을 다시 시작해 보세요.")
            break


play_game()


# print("게임을 다시 하려면 '다시 시작'을 입력해 주세요.\n")
# print("게임을 종료하시겠습니까? (y/n)")
# print("게임을 이어서 하려면 '이어서 하기'를 입력해 주세요.\n")
# print(f"{' Tic Tac Toe 게임을 종료합니다. ':*^52}\n")
