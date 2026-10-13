import unittest

import search
from board import AI, HUMAN, create_board, drop
from search import choose_move, ordered_moves


def play(moves):
    board = create_board()
    player = AI
    for c in moves:
        board = drop(board, c, player)
        player = HUMAN if player == AI else AI
    return board


class TestSearch(unittest.TestCase):
    def test_takes_immediate_win(self):
        board = play([3, 0, 4, 0, 5, 1])
        for algorithm in ("minimax", "alphabeta"):
            move, score = choose_move(board, 3, algorithm)
            self.assertIn(move, (2, 6))
            self.assertGreater(score, search.WIN_SCORE)

    def test_blocks_immediate_loss(self):
        board = play([6, 0, 6, 1, 5, 2])
        for algorithm in ("minimax", "alphabeta"):
            move, _ = choose_move(board, 3, algorithm)
            self.assertEqual(move, 3)

    def test_alphabeta_matches_minimax(self):
        for moves in ([], [3, 3, 2, 4], [3, 3, 2, 2, 4, 4, 1, 5]):
            board = play(moves)
            for depth in range(1, 5):
                mm = choose_move(board, depth, "minimax")
                ab = choose_move(board, depth, "alphabeta")
                self.assertEqual(mm, ab)

    def test_alphabeta_expands_fewer_nodes(self):
        board = create_board()
        search.reset_nodes()
        choose_move(board, 4, "minimax")
        mm_nodes = search.nodes
        search.reset_nodes()
        choose_move(board, 4, "alphabeta")
        self.assertLess(search.nodes, mm_nodes)

    def test_centre_first_ordering(self):
        self.assertEqual(ordered_moves(create_board()), [3, 2, 4, 1, 5, 0, 6])


if __name__ == "__main__":
    unittest.main()
