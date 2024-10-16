from graphics import Point, Line, Window


class Cell():
	def __init__(self, win=None):
		self.has_left_wall = True
		self.has_right_wall = True
		self.has_top_wall = True
		self.has_bottom_wall = True
		self._x1 = None
		self._x2 = None
		self._y1 = None
		self._y2 = None
		self.visited = False
		self.is_Start = True
		self.is_end = False
		self._win = win

	def draw(self, x1, x2, y1, y2):
		if self._win is None:
			return
		self._x1 = x1
		self._x2 = x2
		self._y1 = y1
		self._y2 = y2
		top_left = Point(self._x1, self._y1)
		top_right = Point(self._x2, self._y1)
		bottom_left = Point(self._x1, self._y2)
		bottom_right = Point(self._x2, self._y2)
		if self.has_left_wall:
			colour = "black"
		else:
			colour = "green"
		left_line = Line(top_left, bottom_left)
		self._win.draw_line(left_line, colour)
		if self.has_right_wall:
			colour = "black"
		else:
			colour = "green"
		right_line = Line(top_right, bottom_right)
		self._win.draw_line(right_line, colour)
		if self.has_top_wall:
			colour = "black"
		else:
			colour = "green"
		top_line = Line(top_left, top_right)
		self._win.draw_line(top_line,colour)
		if self.has_bottom_wall:
			colour = "black"
		else:
			colour = "green"
		bottom_line = Line(bottom_left, bottom_right)
		self._win.draw_line(bottom_line,colour)

	def draw_move(self, to_cell, undo=False):
		x1 = (self._x1 + self._x2) / 2
		y1 = (self._y1 + self._y2) / 2
		x2 = (to_cell._x1 + to_cell._x2) / 2
		y2 = (to_cell._y1 + to_cell._y2) / 2
		if undo == True:
			colour = "gray"
		else:
			colour = "red"
		point_a = Point(x1, y1)
		point_b = Point(x2, y2)
		move_line = Line(point_a, point_b)
		self._win.draw_line(move_line, colour)
