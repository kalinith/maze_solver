import random

from tkinter import Tk, BOTH, Canvas
from graphics import Window, Point, Line
from cell import Cell
from maze import Maze

def main():
	window_width = 800
	window_height = 600
	cell_no_columns = 15
	cell_no_rows = 10
	window_margin = 10
	cell_length_x = (window_width - (window_margin * 2)) // cell_no_columns
	cell_length_y = (window_height - (window_margin * 2)) // cell_no_rows

	seed = None

	win = Window(window_width, window_height)

	if seed == None:
		random.seed()
	else:
		random.seed(seed)

	the_maze = Maze(
		window_margin,
		window_margin,
		cell_no_rows,
		cell_no_columns,
		cell_length_x,
		cell_length_y,
		win,
	)

	the_maze.solve()

	win.wait_for_close()



main()
