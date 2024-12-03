def solve_sudoku(board):
    """
    Solves a Sudoku puzzle.
    :param board: List of lists representing a 9x9 Sudoku board.
    :return: Solved board as a list of lists, or None if unsolvable or invalid input.
    """
    # Validate the input board
    if not isinstance(board, list) or len(board) != 9 or any(len(row) != 9 for row in board):
        raise ValueError("Invalid board: Board must be a 9x9 list of lists.")
    for row in board:
        for cell in row:
            if not (isinstance(cell, int) and 0 <= cell <= 9):
                raise ValueError("Invalid board: Board must only contain integers from 0 to 9.")

    def is_valid_move(board, row, col, num):
        for i in range(9):
            if board[row][i] == num or board[i][col] == num:
                return False
        box_row_start, box_col_start = 3 * (row // 3), 3 * (col // 3)
        for i in range(3):
            for j in range(3):
                if board[box_row_start + i][box_col_start + j] == num:
                    return False
        return True

    def solve(board):
        for row in range(9):
            for col in range(9):
                if board[row][col] == 0:  # Empty cell
                    for num in range(1, 10):
                        if is_valid_move(board, row, col, num):
                            board[row][col] = num
                            if solve(board):
                                return True
                            board[row][col] = 0
                    return False
        return True

    if not solve(board):
        return None  # Return None for unsolvable boards
    return board
