EMPTY, AI, HUMAN = 0, 1, 2
ROWS, COLS = 6, 7


def create_board():
    board = [[EMPTY for _ in range(COLS)] for _ in range(ROWS)]
    return board


def is_valid_move(board, col):
    return 0 <= col < COLS and board[ROWS-1][col] == EMPTY


def legal_moves(board):
    return [col for col in range(COLS) if is_valid_move(board, col)]


def drop(board, col, piece):
    new_board = [row[:] for row in board]
    for r in range(ROWS):
        if new_board[r][col] == EMPTY:
            new_board[r][col] = piece
            break
    return new_board


def is_win(board, piece):
    pass


def is_full(board):
    pass


def is_terminal(board):
    pass


def windows(board):
    pass


def print_board(board):
    pass
