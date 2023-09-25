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

victory_rules: list[list[int | str]] = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9],
    [1, 5, 9],
    [3, 5, 7],
]

board_position = deque([1, 2, 3, 4, 5, 6, 7, 8, 9])
random.shuffle(board_position)


def setup_players() -> tuple[str, str]:
    """
    Randomly determines the order of play between two players.

    Returns:
        tuple[str, str]: The first and second player in the shuffled order.
    """
    players = ["computer", "player1"]
    random.shuffle(players)

    first_player = players[0]
    second_player = players[1]
    return first_player, second_player


def is_finished(move: int, symbol: str) -> bool:
    """
    Checks if the game is finished based on the latest move.

    Args:
        move: The board position that was just selected (1 ~ 9).
        symbol: The symbol that was just played ('O' or 'X').

    Returns:
        bool: True if the game is finished (i.e., resulted in a win), otherwise False
    """
    for rule in victory_rules:
        if move in rule:
            rule[rule.index(move)] = symbol

        # current player's win, game over
        if rule.count(symbol) == 3:
            return True
    return False


def select_move_computer(player: str, symbol: str) -> int:
    """
    Automatically selects the move for a computer player.

    Args:
        player: The name of player.
        symbol: The symbol that represents this player in the game ('O' or 'X').

    Returns:
        int: The board position that was just selected (1 ~ 9).
    """
    print(f"{player}님 ({symbol})을 놓을 위치를 선택해 주세요.")

    # Dequeue the next available position
    move = board_position.popleft()
    print(f"{player}님이 선택한 위치는 {move}입니다.\n")
    return move


def input_move_player(player: str, symbol: str) -> int:
    """
    Prompts a human player to select their move.

    Args:
        player: The name of player.
        symbol: The symbol that represents this player in the game ('O' or 'X').

    Returns:
        int: The board position that was just selected (1 ~ 9).
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

                # prevent duplicate moves
                board_position.remove(move)
                break
            else:
                print("이미 수가 놓인 위치를 선택했거나, 1 ~ 9 값을 넘어갔습니다.")
                print("위치를 다시 선택해 주세요.\n")
    return move


def apply_turn(move: int, symbol: str) -> None:
    """
    Applies a player's move to the game board.

    Args:
        move: The board position that was just selected (1 ~ 9).
        symbol: The symbol that was just played ('O' or 'X').
    """
    x, y = game_board_position[move]
    game_board[x][y] = symbol


def play_game() -> None:
    """Run a game between a computer and a human player."""
    # initial game board
    print_game_board()

    first_player, second_player = setup_players()

    print(f"첫 번째 플레이어는 {first_player} (O)입니다.")
    print(f"두 번째 플레이어는 {second_player} (X)입니다.\n")

    if first_player == "computer":
        do_first = select_move_computer
        do_second = input_move_player
    else:
        do_first = input_move_player
        do_second = select_move_computer

    for i in range(9):
        if i % 2 == 0:
            symbol = "O"
            current_player = first_player
            move = do_first(current_player, symbol)
        else:
            symbol = "X"
            current_player = second_player
            move = do_second(current_player, symbol)

        apply_turn(move, symbol)

        # updated game board
        print_game_board()

        if is_finished(move, symbol):
            print(f"{current_player}님 축하합니다!!! {current_player}님이 이겼습니다.")
            break
    else:
        # board is full, draw game
        print("비겼습니다. 게임을 다시 시작해 보세요.")


play_game()


# print("게임을 다시 하려면 '다시 시작'을 입력해 주세요.\n")
# print("게임을 종료하시겠습니까? (y/n)")
# print("게임을 이어서 하려면 '이어서 하기'를 입력해 주세요.\n")
# print(f"{' Tic Tac Toe 게임을 종료합니다. ':*^52}\n")
