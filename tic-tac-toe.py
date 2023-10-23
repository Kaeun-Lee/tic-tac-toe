import random

from player import Computer, Human

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


def initialize_game() -> (
    tuple[list[list[int | str]], dict[int, tuple[int, int]], list[list[int | str]]]
):
    """
    Prepare the game environment.

    Returns:
        game_board: The current state of the game board.
        position_coordinates: A dictionary mapping board positions to their coordinates.
        victory_rules: A list of winning patterns.
    """
    game_board: list[list[int | str]] = []
    position = 1

    for _ in range(3):
        game_board.append([position + j for j in range(3)])
        position += 3

    position_coordinates: dict[int, tuple[int, int]] = {
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
    return game_board, position_coordinates, victory_rules


def print_game_board(game_board: list[list[int | str]]) -> None:
    """Print the current state of the game board."""
    print("<Tic Tac Toe Game Board>")
    for board_row in game_board:
        for j in board_row:
            print(j, end=" ")
        print()
    print()


def setup_players() -> tuple[str, str]:
    """
    Randomly determine the order of play between two players.

    Returns:
        tuple: The first and second player in the shuffled order.
    """
    players = ["computer", "player1"]
    random.shuffle(players)

    first_player = players[0]
    second_player = players[1]
    return first_player, second_player


def switch_player(first_player: str, second_player: str) -> tuple[str, str]:
    """
    Switch the order of two players.

    Returns:
        tuple: The names of players in reversed order.
    """
    first_player, second_player = second_player, first_player
    return first_player, second_player


def is_finished(victory_rules: list[list[int | str]], move: int, symbol: str) -> bool:
    """
    Check if the game is finished based on the latest move.

    Args:
        victory_rules: A list of winning patterns.
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


def apply_turn(
    position_coordinates: dict[int, tuple[int, int]],
    game_board: list[list[int | str]],
    move: int,
    symbol: str,
) -> None:
    """
    Apply a player's move to the game board.

    Args:
        position_coordinates: A dictionary mapping board positions to their coordinates.
        game_board: The current state of the game board.
        move: The board position that was just selected (1 ~ 9).
        symbol: The symbol that was just played ('O' or 'X').
    """
    x, y = position_coordinates[move]
    game_board[x][y] = symbol


def restart_game() -> bool:
    """
    Prompt the player to restart game.

    Returns:
        bool: True for restart, otherwise False.
    """
    while True:
        play_again = input("게임을 다시 하시겠습니까? (y/n) : ")
        print()
        if play_again in "yn":
            break
        else:
            print("잘못된 값을 입력했습니다. y/n 중 하나를 입력해 주세요.\n")
    return play_again == "y"


def play_game(
    rounds_count: int, first_player: str, second_player: str
) -> tuple[str, str]:
    """
    Run a game of Tic Tac Toe between two players.

    Args:
        rounds_count: The current round number.
        first_player: The first player's name in this round.
        second_player: The second player's name in this round.
    Returns:
        tuple: The names of the first and second players.
    """
    print(f'"Round {rounds_count}"\n')

    # display initial game board
    print_game_board(game_board)

    # switch player order if not the first round
    if rounds_count != 1:
        first_player, second_player = switch_player(first_player, second_player)

    print(f"첫 번째 플레이어는 {first_player} (O)입니다.")
    print(f"두 번째 플레이어는 {second_player} (X)입니다.\n")

    computer = Computer("computer")
    player1 = Human("player1")

    if first_player == "computer":
        do_first = computer.select_move
        do_second = player1.select_move
    else:
        do_first = player1.select_move
        do_second = computer.select_move

    for i in range(9):
        if i % 2 == 0:
            symbol = "O"
            current_player = first_player
            move = do_first(available_moves)
        else:
            symbol = "X"
            current_player = second_player
            move = do_second(available_moves)

        apply_turn(position_coordinates, game_board, move, symbol)

        # updated game board
        print_game_board(game_board)

        if is_finished(victory_rules, move, symbol):
            print(f"{current_player}님 축하합니다!!! {current_player}님이 이겼습니다.")
            break
    else:
        # board is full, draw game
        print("비겼습니다. 게임을 다시 시작해 보세요.\n")
    return first_player, second_player


# initialize variables and start playing game
rounds_count = 1
game_board, position_coordinates, victory_rules = initialize_game()
available_moves = set(range(1, 10))
first_player, second_player = setup_players()

first_player, second_player = play_game(rounds_count, first_player, second_player)

while restart_game():
    rounds_count += 1
    game_board, position_coordinates, victory_rules = initialize_game()
    available_moves = set(range(1, 10))
    first_player, second_player = play_game(rounds_count, first_player, second_player)
print()
print(f"{' Tic Tac Toe 게임을 종료합니다. ':*^52}\n")
