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
print("computer님, (O)를 놓을 위치를 선택해 주세요.\n")

game_board = []
position = 1

for _ in range(3):
    game_board.append([str(position + j) for j in range(3)])
    position += 3


for board_row in game_board:
    for j in board_row:
        print(j, end=" ")
    print()
print()

game_board[1][1] = "O"

print("player1님, (X)를 놓을 위치를 선택해 주세요.\n")
for board_row in game_board:
    for j in board_row:
        print(j, end=" ")
    print()
print()

game_board[1][0] = "X"

print("computer님, (O)를 놓을 위치를 선택해 주세요.\n")
for board_row in game_board:
    for j in board_row:
        print(j, end=" ")
    print()
print()


print("축하합니다!! computer님이 이겼습니다!\n")
print("비겼습니다. 게임을 다시 시작해 보세요.")
print("게임을 다시 하려면 '다시 시작'을 입력해 주세요.\n")

print("게임을 종료하시겠습니까? (y/n)")
print("게임을 이어서 하려면 '이어서 하기'를 입력해 주세요.\n")
print(f"{' Tic Tac Toe 게임을 종료합니다. ':*^52}\n")
