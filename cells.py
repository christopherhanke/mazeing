from graphics import Line, Point

class Cell():
    def __init__(self, x1, y1, x2, y2, window):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        self._win = window
    
    def draw(self):
        if self.has_left_wall:
            self._win.draw_line(Line(Point(self._x1, self._y1), Point(self._x1, self._y2)), "black")
        if self.has_top_wall:
            self._win.draw_line(Line(Point(self._x1, self._y1), Point(self._x2, self._y1)), "black")
        if self.has_right_wall:
            self._win.draw_line(Line(Point(self._x2, self._y1), Point(self._x2, self._y2)), "black")
        if self.has_bottom_wall:
            self._win.draw_line(Line(Point(self._x1, self._y2), Point(self._x2, self._y2)), "black")
    
    def draw_move(self, to_cell, undo=False):
        color = "red"
        if undo:
            color = "gray"
        
        half_length = abs(self._x2 - self._x1) // 2
        x_center = half_length + self._x1
        y_center = half_length + self._y1

        half_length2 = abs(to_cell._x2 - to_cell._x1) // 2
        x_center2 = half_length2 + to_cell._x1
        y_center2 = half_length2 + to_cell._y1

        self._win.draw_line(
            Line(
                Point(x_center, y_center),
                Point(x_center2, y_center2)
            ),
            color
        )
