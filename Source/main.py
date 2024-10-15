import random

from tkinter import Tk, BOTH, Canvas
from graphics import Window, Point, Line
from cell import Cell
from maze import Maze

def main():
	window_width = 800
	window_height = 600
	cell_length_x = 40
	cell_length_y = 40
	cell_start_x = 200
	cell_start_y = 100
	cell_no_columns = 10
	cell_no_rows = 10
	seed = 0 #None

	win = Window(window_width, window_height)

	if seed == None:
		random.seed()
	else:
		random.seed(seed)

	the_maze = Maze(
		cell_start_x,
		cell_start_y,
		cell_no_rows,
		cell_no_columns,
		cell_length_x,
		cell_length_y,
		win,
	)

	win.wait_for_close()



main()
