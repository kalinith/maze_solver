from tkinter import Tk, BOTH, Canvas
from graphics import Window, Point, Line
from cell import Cell

def main():
	win = Window(800,600)
	for i in range(0,800,50):
		for j in range(0,600,50):
			k = i + 50
			l = j + 50

			cell = Cell(win)
			cell.draw(i, k, j, l)

#			pointa = Point(i,j)
#			pointb = Point(i,j+30)
#			line = Line(pointa, pointb)
#			win.draw_line(line, "black")


	win.wait_for_close()



main()
