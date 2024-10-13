from tkinter import Tk, BOTH, Canvas

class Window():
	def __init__(self,width,height):
		self.__root = Tk()
		self.__root.title = "Maze Solver"
		self.__root.protocol("WM_DELETE_WINDOW", self.close)
		self.__canvas = Canvas(self.__root, bg="green", height=height,width=width)
		self.__canvas.pack()
		self.__is_running = False

	def draw_line(self, line, colour="black"):
		line.draw(self.__canvas, colour)

	def redraw(self):
		self.__root.update_idletasks()
		self.__root.update()

	def wait_for_close(self):
		self.__is_running = True
		while self.__is_running:
			self.redraw()

	def close(self):
		self.__is_running = False

class Point():
	def __init__(self,x=0,y=0):
		self.x = x
		self.y = y

class Line():
	def __init__(self,a, b):
		self.a = a
		self.b = b

	def draw(self, canvas, colour="black"):
		canvas.create_line(self.a.x, self.a.y, self.b.x, self.b.y, fill=colour, width=2)
		

