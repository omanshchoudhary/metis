import argparse
import sys
import time

import search
from board import AI, HUMAN, COLS, create_board, drop, is_valid_move, is_win, is_full, print_board


def parse_args():
    parser = argparse.ArgumentParser(description="Play Connect Four against Metis.")
    parser.add_argument("--depth", type=int, default=6, help="search depth (default 6)")
    parser.add_argument("--first", choices=["human", "ai"], default="human", help="who moves first")
    parser.add_argument("--algorithm", choices=["alphabeta", "minimax"], default="alphabeta")
    parser.add_argument("--moves", default="", help="start position as columns played in order, e.g. 3324")
    parser.add_argument("--once", action="store_true", help="print the AI's move for the position and exit")
    return parser.parse_args()


def other(player):
    return HUMAN if player == AI else AI


def setup(moves, first):
    board = create_board()
    player = AI if first == "ai" else HUMAN
    for ch in moves:
        if not ch.isdigit() or not is_valid_move(board, int(ch)):
            sys.exit(f"invalid move '{ch}' in --moves")
        board = drop(board, int(ch), player)
        if is_win(board, player):
            sys.exit("--moves already contains a finished game")
        player = other(player)
    return board, player


def ai_turn(board, depth, algorithm):
    search.reset_nodes()
    start = time.perf_counter()
    col, score = search.choose_move(board, depth, algorithm)
    elapsed = time.perf_counter() - start
    print(f"AI plays column {col}  (score {score}, {search.nodes} nodes, {elapsed:.3f}s)")
    return col


def human_turn(board):
    while True:
        text = input(f"your move (0-{COLS - 1}, q to quit): ").strip()
        if text == "q":
            sys.exit(0)
        if text.isdigit() and is_valid_move(board, int(text)):
            return int(text)
        print("not a legal column")


def main():
    args = parse_args()
    board, player = setup(args.moves, args.first)
    print_board(board)

    if args.once:
        if player != AI:
            sys.exit("it is the human's turn in this position")
        ai_turn(board, args.depth, args.algorithm)
        return

    while True:
        if player == AI:
            col = ai_turn(board, args.depth, args.algorithm)
        else:
            col = human_turn(board)
        board = drop(board, col, player)
        print()
        print_board(board)

        if is_win(board, player):
            print("AI wins" if player == AI else "you win")
            return
        if is_full(board):
            print("draw")
            return
        player = other(player)


if __name__ == "__main__":
    main()
