import time
import random

from graphics import Window
from cell import Cell

class Maze():
	def __init__(
			self,
			x1,
			y1,
			num_rows,
			num_cols,
			cell_size_x,
			cell_size_y,
			win=None,
	):
		self._cells = []
		self._x1 = x1
		self._y1 = y1
		self._num_rows = num_rows
		self._num_cols = num_cols
		self._cell_size_x = cell_size_x
		self._cell_size_y = cell_size_y
		self._win = win

		self._create_cells()
		self._break_entrance_and_exit()
		self._break_walls_r(0, 0)


	def _create_cells(self):
		for i in range(self._num_cols):
			col_list = []
			for j in range(self._num_rows):
				cell = Cell(self._win)
				col_list.append(cell)
			self._cells.append(col_list)
		for i in range(len(self._cells)):
			for j in range(len(self._cells[i])):
				self._draw_cell(i, j)

	def _break_entrance_and_exit(self):
		self._cells[0][0].has_top_wall = False
		self._draw_cell(0,0)
		self._cells[self._num_cols-1][self._num_rows-1].has_bottom_wall = False
		self._draw_cell(self._num_cols-1,self._num_rows-1)

	def _break_walls_r(self,i,j):
		self._cells[i][j].visited = True
		while True:
			places_to_go = []
			if i > 0:
				if self._cells[i-1][j].visited == False:
					tp = (i-1,j)
					places_to_go.append(tp)
			if i < len(self._cells) - 1:
				if self._cells[i+1][j].visited == False:
					tp = (i+1,j)
					places_to_go.append(tp)
			if j > 0:
				if self._cells[i][j-1].visited == False:
					tp = (i,j-1)
					places_to_go.append(tp)
			if j < len(self._cells[i]) -1:
				if self._cells[i][j+1].visited == False:
					tp = (i,j+1)
					places_to_go.append(tp)
			print(places_to_go)

			if places_to_go == []:
				self._draw_cell(i, j)
				return

			direction = random.randrange(len(places_to_go))
			x, y = places_to_go[direction]
			if x < i:
				#left wall
				self._cells[i][j].has_left_wall = False
				self._cells[x][y].has_right_wall = False
			if x > i:
				self._cells[i][j].has_right_wall = False
				self._cells[x][y].has_left_wall = False
			if x == i and y < j:
				self._cells[i][j].has_top_wall = False
				self._cells[x][y].has_bottom_wall = False
			if x == i and y > j:
				self._cells[i][j].has_bottom_wall = False
				self._cells[x][y].has_top_wall = False
			self._break_walls_r(x, y)
			


	def _draw_cell(self, i, j):
		if self._win is None:
			return
		cell = self._cells[i][j]
		x1 = self._x1 + (self._cell_size_x * i)
		y1 = self._y1 + (self._cell_size_y * j)
		x2 = x1 + self._cell_size_x
		y2 = y1 + self._cell_size_y
		cell.draw(x1, x2, y1, y2)
		self._animate()


	def _animate(self):
		if self._win is None:
			return
		self._win.redraw()
		time.sleep(0.05)



#     0 1 2 3 4 ... x (increases to the right)
#   0 +----->
#	1 |
#	2 |
#	3 |
#	4 |
#	. V
#	. y (increases downward)