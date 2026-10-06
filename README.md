# Metis

Connect Four AI in pure Python using minimax with alpha-beta pruning and a hand-built evaluation function.

Metis plays Connect Four against a human. On each turn it searches the game tree a fixed number of moves ahead, assumes the opponent always plays their best reply, and picks the move with the best guaranteed outcome. Positions at the depth cutoff are scored by a heuristic evaluation function.

> **Status:** in progress. The board engine is complete. Evaluation and search are under development.

## How it works

| Component | Role |
|---|---|
| **State** | 6×7 grid of empty / AI / human cells, plus the player to move |
| **Actions** | Drop a piece into any non-full column (at most 7) |
| **Transition** | The piece falls to the lowest empty cell in that column |
| **Terminal test** | Four in a row (horizontal, vertical or diagonal), or a full board |
| **Utility** | Win = +1,000,000, loss = −1,000,000, draw = 0, with remaining depth added so faster wins score higher |
| **Search** | Depth-limited minimax (AI = MAX, human = MIN) with alpha-beta pruning and move ordering |

### Evaluation function

The board contains exactly 69 four-cell windows (24 horizontal, 21 vertical, 24 diagonal). Each window is scored from the AI's point of view:

| Window | Score |
|---|---|
| 3 AI + 1 empty | +5 |
| 2 AI + 2 empty | +2 |
| 3 human + 1 empty | −4 |
| Mixed or otherwise | 0 |

Each AI piece in the centre column adds +3. A second evaluation function (Eval 2) adds extra weight for open-ended threats and a larger penalty for unblocked opponent threes.

## Project structure

```
metis/
├── board.py          board state, legal moves, drop, win check, windows
├── evaluate.py       evaluation functions
├── search.py         minimax, alpha-beta, move ordering
├── main.py           command-line game, human vs AI
├── experiments.py    node counts, timings, head-to-head games
└── tests/
```

The board is a list of 6 rows of 7 integers, with row 0 at the bottom. `EMPTY`, `AI` and `HUMAN` are `0`, `1` and `2`. `drop()` returns a new board rather than mutating the old one, so the search can explore moves without undoing them.

## Requirements

Python 3. No third-party packages: the AI uses only the standard library.

## Usage

```bash
git clone <repo-url>
cd metis
python3 main.py
```

Run the tests:

```bash
python3 -m unittest discover tests
```

## Experiments

1. **Minimax vs alpha-beta:** nodes expanded and time per move at depths 2–6. Both must return the same move, which confirms that pruning is correct.
2. **Eval 1 vs Eval 2:** win rate over 50 games at the same depth, alternating who moves first.
