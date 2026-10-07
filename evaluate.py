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
