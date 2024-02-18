def human_move(board):
    """
    Ask the human player for their move and return the updated board.

    Args:
        board (list): The current state of the game board.

    Returns:
        list: The updated game board after the human player's move.
    """
    move = -1
    while move < 0 or move >= len(board[0]) or board[0][move] != 0:
        try:
            move = int(input("Enter your column choice (0-6): "))
            if board[0][move] != 0:
                print("Column is full, try another one.")
                move = -1  
        except ValueError:
            print("Invalid input, please enter a number.")
        except IndexError:
            print("Column out of bounds, please choose between 0-6.")
    for i in range(len(board)):
        if board[i][move] != 0:
            board[i-1][move] = -1  
            break
    else:
        board[len(board)-1][move] = -1  
    return board