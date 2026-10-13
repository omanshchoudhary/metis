from board import AI, HUMAN, COLS, legal_moves, drop, is_win
from evaluate import evaluate

WIN_SCORE = 1_000_000
INF = float("inf")

nodes = 0


def reset_nodes():
    global nodes
    nodes = 0


def ordered_moves(board):
    centre = COLS // 2
    return sorted(legal_moves(board), key=lambda col: abs(col - centre))


def terminal_score(board, depth):
    if is_win(board, AI):
        return WIN_SCORE + depth
    if is_win(board, HUMAN):
        return -WIN_SCORE - depth
    if not legal_moves(board):
        return 0
    return None


def minimax(board, depth, maximizing, eval_fn=evaluate):
    global nodes
    nodes += 1

    score = terminal_score(board, depth)
    if score is not None:
        return score, None
    if depth == 0:
        return eval_fn(board), None

    moves = ordered_moves(board)
    best_move = moves[0]

    if maximizing:
        best_score = -INF
        for col in moves:
            score, _ = minimax(drop(board, col, AI), depth - 1, False, eval_fn)
            if score > best_score:
                best_score, best_move = score, col
    else:
        best_score = INF
        for col in moves:
            score, _ = minimax(drop(board, col, HUMAN), depth - 1, True, eval_fn)
            if score < best_score:
                best_score, best_move = score, col

    return best_score, best_move


def alphabeta(board, depth, alpha, beta, maximizing, eval_fn=evaluate):
    global nodes
    nodes += 1

    score = terminal_score(board, depth)
    if score is not None:
        return score, None
    if depth == 0:
        return eval_fn(board), None

    moves = ordered_moves(board)
    best_move = moves[0]

    if maximizing:
        best_score = -INF
        for col in moves:
            score, _ = alphabeta(drop(board, col, AI), depth - 1, alpha, beta, False, eval_fn)
            if score > best_score:
                best_score, best_move = score, col
            alpha = max(alpha, best_score)
            if alpha >= beta:
                break
    else:
        best_score = INF
        for col in moves:
            score, _ = alphabeta(drop(board, col, HUMAN), depth - 1, alpha, beta, True, eval_fn)
            if score < best_score:
                best_score, best_move = score, col
            beta = min(beta, best_score)
            if alpha >= beta:
                break

    return best_score, best_move


def choose_move(board, depth, algorithm="alphabeta", eval_fn=evaluate):
    if algorithm == "minimax":
        score, move = minimax(board, depth, True, eval_fn)
    else:
        score, move = alphabeta(board, depth, -INF, INF, True, eval_fn)
    return move, score
