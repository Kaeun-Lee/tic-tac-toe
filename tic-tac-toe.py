import random

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
    print("<Tic Tac Toe Game Board>")
    for board_row in game_board:
        for j in board_row:
            print(j, end=" ")
        print()
    print()


print_game_board()

# 사용자 입력 없이 랜덤으로 고른 위치에 O, X 수를 두고 결과를 출력한다.
# 한 플레이어가 랜덤으로 정수를 선택하고 그 자리에 O나 X가 없으면 해당하는 수를 둔다.

game_board_position = {
    "1": (0, 0),
    "2": (0, 1),
    "3": (0, 2),
    "4": (1, 0),
    "5": (1, 1),
    "6": (1, 2),
    "7": (2, 0),
    "8": (2, 1),
    "9": (2, 2),
}

computer_symbol = "O"
player1_symbol = "X"


def choice_move(player, symbol):
    print(f"{player}님 ({symbol})을 놓을 위치를 선택해 주세요.")
    player_move = str(random.randint(1, 9))
    x, y = game_board_position[player_move]

    if game_board[x][y] not in "OX":
        print(f"{player}님이 선택한 위치는 {player_move}입니다.\n")
        game_board[x][y] = symbol
    else:
        print("수를 놓을 수 없는 자리입니다. 다시 선택해 주세요.\n")


# test
move_count = 0
while move_count < 9:
    choice_move("computer", computer_symbol)
    print_game_board()
    choice_move("player1", player1_symbol)
    print_game_board()
    move_count += 1


print("축하합니다!! computer님이 이겼습니다!\n")
print("비겼습니다. 게임을 다시 시작해 보세요.")
print("게임을 다시 하려면 '다시 시작'을 입력해 주세요.\n")

print("게임을 종료하시겠습니까? (y/n)")
print("게임을 이어서 하려면 '이어서 하기'를 입력해 주세요.\n")
print(f"{' Tic Tac Toe 게임을 종료합니다. ':*^52}\n")
