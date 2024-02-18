from board import Board
from human import human_move
from MTCS import *
from utils import *
import sys

def print_board(board):
    """
    Prints the current state of the game board.

    Args:
    - board (list): The game board.

    Returns:
    - None
    """
    for row in board:
        print(' '.join(['X' if cell == 1 else 'O' if cell == -1 else '.' for cell in row]))
    print()

def play_game(depth=1000):
    """
    Plays a game of Connect 4.

    Args:
    - depth (int): The depth of the Monte Carlo Tree Search algorithm. Default is 1000.

    Returns:
    - None
    """
    board = [[0 for _ in range(7)] for _ in range(6)]
    game_board = Board(board)
    player_turn = False

    while True:
        if player_turn:
            print_board(game_board.board)
            game_board.board = human_move(game_board.board)
        else:
            best_move_col = find_best_move(game_board, depth=depth)
            row = game_board.try_move(best_move_col)
            if row != -1:
                game_board.board[row][best_move_col] = 1
            print_board(game_board.board)

        winner = game_board.winner()
        if winner != 0 or game_board.terminal():
            print_board(game_board.board)
            break

        player_turn = not player_turn

    if winner == 1:
        print("AI wins!")
    elif winner == -1:
        print("Human wins!")
    else:
        print("It's a draw!")

def find_best_move(board, depth=1000):
    """
    Finds the best move using the Monte Carlo Tree Search algorithm.

    Args:
    - board (Board): The current game board.
    - depth (int): The depth of the Monte Carlo Tree Search algorithm. Default is 1000.

    Returns:
    - The column index of the best move.
    """
    factor = 2.0
    o = Node(board)
    bestMove = MTCS(depth, o, factor)
    bbb = deepcopy(bestMove.state)
    return bbb.get_last_move()[1]

if len(sys.argv) > 1:
    depth = int(sys.argv[1])
    play_game(depth=depth)
else:
    play_game(depth=3000)
