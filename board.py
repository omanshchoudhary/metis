EMPTY, AI, HUMAN = 0, 1, 2
ROWS, COLS = 6, 7


def create_board():
    board = [[EMPTY for _ in range(COLS)] for _ in range(ROWS)]
    return board


def is_valid_move(board, col):
    return 0 <= col < COLS and board[ROWS - 1][col] == EMPTY


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
    for w in windows(board):
        if w == [piece] * 4:
            return True
    return False


def is_full(board):
    return legal_moves(board) == []


def is_terminal(board):
    return is_win(board, AI) or is_win(board, HUMAN) or is_full(board)


def windows(board):
    result = []
    for dr, dc in [(0, 1), (1, 0), (1, 1), (-1, 1)]:
        for r in range(ROWS):
            for c in range(COLS):
                end_r = r + 3 * dr
                end_c = c + 3 * dc
                if 0 <= end_r < ROWS and 0 <= end_c < COLS:
                    result.append([board[r + i * dr][c + i * dc] for i in range(4)])
    return result


def print_board(board):
    pass
