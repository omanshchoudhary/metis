from board import windows, ROWS, COLS, EMPTY, AI, HUMAN


def evaluate(board):
    score = 0

    for window in windows(board):
        ai_count = window.count(AI)
        human_count = window.count(HUMAN)
        empty_count = window.count(EMPTY)

        if ai_count == 3 and empty_count == 1:
            score += 5
        elif ai_count == 2 and empty_count == 2:
            score += 2
        elif human_count == 3 and empty_count == 1:
            score -= 4

    for row in range(ROWS):
        if board[row][COLS // 2] == AI:
            score += 3

    return score


def is_playable(board, row, col):
    if not (0 <= row < ROWS and 0 <= col < COLS):
        return False

    if board[row][col] != EMPTY:
        return False

    # A piece can be played in the bottom row,
    # or directly above an already occupied cell.
    return row == 0 or board[row - 1][col] != EMPTY


def open_ended_threats(board, piece):
    count = 0

    directions = [
        (0, 1),
        (1, 0),
        (1, 1),
        (1, -1)
    ]

    for r in range(ROWS):
        for c in range(COLS):
            for dr, dc in directions:
                cells = []

                for i in range(4):
                    nr = r + i * dr
                    nc = c + i * dc

                    if 0 <= nr < ROWS and 0 <= nc < COLS:
                        cells.append(board[nr][nc])
                    else:
                        break

                if cells != [EMPTY, piece, piece, EMPTY]:
                    continue

                left_r = r
                left_c = c

                right_r = r + 3 * dr
                right_c = c + 3 * dc

                left_playable = is_playable(board, left_r, left_c)
                right_playable = is_playable(board, right_r, right_c)

                if left_playable or right_playable:
                    count += 1

    return count


def evaluate2(board):
    score = 0

    for window in windows(board):
        ai_count = window.count(AI)
        human_count = window.count(HUMAN)
        empty_count = window.count(EMPTY)

        if ai_count == 3 and empty_count == 1:
            score += 8
        elif ai_count == 2 and empty_count == 2:
            score += 2
        elif human_count == 3 and empty_count == 1:
            score -= 7

    for row in range(ROWS):
        if board[row][COLS // 2] == AI:
            score += 3

    score += open_ended_threats(board, AI)

    return score