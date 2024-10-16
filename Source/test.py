import unittest
import random
from maze import Maze


class Tests(unittest.TestCase):
	def test_maze_create_cells(self):
		num_cols = 12
		num_rows = 10
		m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
		self.assertEqual(
			len(m1._cells),
			num_cols,
		)
		self.assertEqual(
			len(m1._cells[0]),
			num_rows,
		)

	def test_maze_create_cells_large(self):
		num_cols = 16
		num_rows = 12
		m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
		self.assertEqual(
			len(m1._cells),
			num_cols,
		)
		self.assertEqual(
			len(m1._cells[0]),
			num_rows,
		)

	def test_maze_create_cells_x_large(self):
		num_cols = 32
		num_rows = 24
		m1 = Maze(0, 0, num_rows, num_cols, 8, 8)
		self.assertEqual(
			len(m1._cells),
			num_cols,
		)
		self.assertEqual(
			len(m1._cells[0]),
			num_rows,
		)

	def test_maze_break_entrance_and_exit(self):
		num_cols = 12
		num_rows = 10
		m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
		self.assertEqual(
			m1._cells[0][0].has_top_wall,
			False,
		)
		self.assertEqual(
			m1._cells[num_cols - 1][num_rows - 1].has_bottom_wall,
			False,
		)

	def test_break_walls_r(self):
		num_cols = 10
		num_rows = 10
		random.seed(0)
		m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
		m1._break_walls_r(0,0)

		self.assertEqual(
			m1._cells[4][4].has_top_wall,
			False,
		)

		self.assertEqual(
			m1._cells[4][4].has_left_wall,
			False,
		)

	def test_reset_visited(self):
		num_cols = 12
		num_rows = 10
		m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
		self.assertEqual(
			m1._cells[5][5].visited,
			False,
		)


if __name__ == "__main__":
	unittest.main()		


