import unittest

from board import AI, HUMAN, create_board, drop
from evaluate import evaluate


class TestEvaluate(unittest.TestCase):

    def test_empty_board(self):
        board = create_board()
        self.assertEqual(evaluate(board), 0)

    def test_center_ai_piece(self):
        board = create_board()
        board = drop(board, 3, AI)
        self.assertEqual(evaluate(board), 3)

    def test_three_ai_pieces(self):
        board = create_board()

        for col in [0, 1, 2]:
            board = drop(board, col, AI)

        self.assertEqual(evaluate(board), 7)

    def test_three_human_pieces(self):
        board = create_board()

        for col in [0, 1, 2]:
            board = drop(board, col, HUMAN)

        self.assertEqual(evaluate(board), -4)


if __name__ == "__main__":
    unittest.main()