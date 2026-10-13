import unittest

from board import EMPTY, AI, HUMAN, ROWS, COLS, create_board, drop, is_valid_move, legal_moves, is_win, is_full, windows


def fill(board, cols, piece):
    for c in cols:
        board = drop(board, c, piece)
    return board


class TestBoard(unittest.TestCase):
    def test_create_board(self):
        board = create_board()
        self.assertEqual(len(board), ROWS)
        self.assertTrue(all(len(row) == COLS and set(row) == {EMPTY} for row in board))

    def test_drop_stacks_and_copies(self):
        board = create_board()
        after = drop(drop(board, 3, AI), 3, HUMAN)
        self.assertEqual(board[0][3], EMPTY)
        self.assertEqual(after[0][3], AI)
        self.assertEqual(after[1][3], HUMAN)

    def test_valid_moves(self):
        board = fill(create_board(), [0] * ROWS, AI)
        self.assertFalse(is_valid_move(board, 0))
        self.assertFalse(is_valid_move(board, -1))
        self.assertFalse(is_valid_move(board, COLS))
        self.assertEqual(legal_moves(board), list(range(1, COLS)))

    def test_window_count(self):
        self.assertEqual(len(windows(create_board())), 69)

    def test_wins(self):
        board = create_board()
        self.assertTrue(is_win(fill(board, [0, 1, 2, 3], AI), AI))
        self.assertTrue(is_win(fill(board, [5] * 4, HUMAN), HUMAN))
        self.assertFalse(is_win(fill(board, [0, 1, 2], AI), AI))

    def test_diagonal_win(self):
        board = create_board()
        board = drop(board, 1, AI)
        board = fill(board, [2], HUMAN)
        board = drop(board, 2, AI)
        board = fill(board, [3, 3], HUMAN)
        board = drop(board, 3, AI)
        board = fill(board, [4, 4, 4], HUMAN)
        board = drop(board, 4, AI)
        self.assertTrue(is_win(board, AI))

    def test_full(self):
        board = create_board()
        self.assertFalse(is_full(board))
        for c in range(COLS):
            for r in range(ROWS):
                board = drop(board, c, AI if (r // 2 + c) % 2 == 0 else HUMAN)
        self.assertTrue(is_full(board))


if __name__ == "__main__":
    unittest.main()
