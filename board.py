import random
from copy import deepcopy


class Board(object):
    def __init__(self, board, last_move=[None, None]):
        """
        Initialize the Board object.

        Args:
        - board: 2D list representing the game board.
        - last_move: List representing the last move made on the board.
        """
        self.board = board
        self.last_move = last_move

    def try_move(self, move):
        """
        Check if a move is valid.

        Args:
        - move: Integer representing the column where the move is made.

        Returns:
        - Integer: -1 if the move is invalid, otherwise the row where the move is made.
        """
        if move < 0 or move > 7 or self.board[0][move] != 0:
            return -1

        for i in range(len(self.board)):
            if self.board[i][move] != 0:
                return i - 1
        return len(self.board) - 1

    def terminal(self):
        """
        Check if the game has reached a terminal state.

        Returns:
        - Boolean: True if the game is in a terminal state, False otherwise.
        """
        for i in range(len(self.board[0])):
            if self.board[0][i] == 0:
                return False
        return True

    def get_board(self):
        """
        Get the current game board.

        Returns:
        - 2D list: The current game board.
        """
        return self.board

    def legal_moves(self):
        """
        Get a list of possible moves that can be made.

        Returns:
        - List: A list of possible moves.
        """
        legal = []
        for i in range(len(self.board[0])):
            if self.board[0][i] == 0:
                legal.append(i)
        return legal

    def next_state(self, turn):
        """
        Get the next state of the game.

        Args:
        - turn: Integer representing the player's turn.

        Returns:
        - Board: The next state of the game.
        """
        aux = deepcopy(self)
        moves = aux.legal_moves()
        if len(moves) > 0:
            ind = random.randint(0, len(moves) - 1)
            row = aux.try_move(moves[ind])
            aux.board[row][moves[ind]] = turn
            aux.last_move = [row, moves[ind]]
        return aux

    def get_last_move(self):
        """
        Get the last move made on the board.

        Returns:
        - List: The last move made on the board.
        """
        print(self.last_move)
        return self.last_move

    def winner(self):
        """
        Check if there is a winner in the game.

        Returns:
        - Integer: The player number if there is a winner, 0 otherwise.
        """
        dx = [0, 1, 1, -1]  # Directions: Right, Down, Diagonal down-right, Diagonal down-left
        dy = [1, 0, 1, 1]
        for x in range(len(self.board)):
            for y in range(len(self.board[0])):
                if self.board[x][y] != 0:  # Skip empty cells
                    player = self.board[x][y]
                    for d in range(4):
                        nx, ny = x, y
                        win = True
                        for _ in range(3):  # Need to match 3 more pieces
                            nx += dx[d]
                            ny += dy[d]
                            if (
                                nx >= len(self.board)
                                or ny >= len(self.board[0])
                                or ny < 0
                                or self.board[nx][ny] != player
                            ):
                                win = False
                                break
                        if win:
                            return player
        return 0  # No winner yet
