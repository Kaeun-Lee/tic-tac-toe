import random
from itertools import cycle

from board import Board
from player import Computer, Human, Player


def setup_players() -> tuple[Player, Player]:
    """
    Determines the order of play between two players.

    Returns:
        The first and second player in the shuffled order.
    """
    players = [Human("player1"), Computer("computer")]
    random.shuffle(players)
    return players[0], players[1]


def restart_game() -> bool:
    """
    Prompts the player to restart game.

    Return:
        True for restart, False otherwise.
    """
    while True:
        play_again = input("게임을 다시 하시겠습니까? (y/n) : ")
        print()
        if play_again in ["y", "n"]:
            break
        else:
            print("잘못된 값을 입력했습니다. y/n 중 하나를 입력해 주세요.\n")
    return play_again == "y"


def play_one_round(
    board: Board,
    first_player: Player,
    second_player: Player,
) -> None:
    """
    Runs a game of Tic Tac Toe between two players.

    Args:
        board: The game board in this round.
        first_player: The first player in this round.
        second_player: The second player in this round.
    """
    # Display initial game board
    print(board)

    print(f"첫 번째 플레이어는 {first_player.name} (O)입니다.")
    print(f"두 번째 플레이어는 {second_player.name} (X)입니다.\n")

    symbol_player_pairs = cycle([("O", first_player), ("X", second_player)])

    for _ in range(len(board._current_state)):
        symbol, current_player = next(symbol_player_pairs)
        move = current_player.select_move(board.get_available_moves())

        board.apply_turn(move, symbol)

        # Updated game board
        print(board)

        if board.is_finished():
            print(f"{current_player.name}님 축하합니다!!! {current_player.name}님이 이겼습니다.\n")
            return
    # Board is full, draw game
    print("비겼습니다. 게임을 다시 시작해 보세요.\n")


def main() -> None:
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

    # Initialize variables and start playing game
    rounds_count = 1
    board = Board()
    first_player, second_player = setup_players()

    while True:
        print(f'"Round {rounds_count}"\n')
        play_one_round(board, first_player, second_player)
        if restart_game():
            rounds_count += 1
            board.reset()
            first_player, second_player = second_player, first_player
        else:
            break
    print(f"{' Tic Tac Toe 게임을 종료합니다. ':*^52}\n")


if __name__ == "__main__":
    main()
