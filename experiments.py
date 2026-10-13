import argparse
import csv
import os
import time

import search
from board import AI, HUMAN, create_board, drop

POSITIONS = {
    "empty": "",
    "opening": "3324",
    "midgame": "34233245",
}


def build(moves):
    board = create_board()
    player = AI
    for ch in moves:
        board = drop(board, int(ch), player)
        player = HUMAN if player == AI else AI
    return board


def measure(board, depth, algorithm):
    search.reset_nodes()
    start = time.perf_counter()
    move, score = search.choose_move(board, depth, algorithm)
    return move, score, search.nodes, time.perf_counter() - start


def experiment_a(min_depth, max_depth, out_path):
    rows = []
    header = f"{'position':<9} {'depth':>5} {'mm move':>7} {'ab move':>7} {'mm nodes':>9} {'ab nodes':>9} {'mm time':>8} {'ab time':>8} same"
    print(header)
    for name, moves in POSITIONS.items():
        board = build(moves)
        for depth in range(min_depth, max_depth + 1):
            mm = measure(board, depth, "minimax")
            ab = measure(board, depth, "alphabeta")
            same = mm[0] == ab[0] and mm[1] == ab[1]
            print(f"{name:<9} {depth:>5} {mm[0]:>7} {ab[0]:>7} {mm[2]:>9} {ab[2]:>9} {mm[3]:>8.3f} {ab[3]:>8.3f} {same}")
            rows.append([name, depth, mm[0], ab[0], mm[1], ab[1], mm[2], ab[2], round(mm[3], 4), round(ab[3], 4), same])

    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["position", "depth", "minimax_move", "alphabeta_move", "minimax_score", "alphabeta_score",
                         "minimax_nodes", "alphabeta_nodes", "minimax_time", "alphabeta_time", "same_move"])
        writer.writerows(rows)
    print(f"\nwrote {out_path}")


def main():
    parser = argparse.ArgumentParser(description="Minimax vs alpha-beta: nodes and time per move.")
    parser.add_argument("--min-depth", type=int, default=2)
    parser.add_argument("--max-depth", type=int, default=6)
    parser.add_argument("--out", default="results/experiment_a.csv")
    args = parser.parse_args()
    experiment_a(args.min_depth, args.max_depth, args.out)


if __name__ == "__main__":
    main()
