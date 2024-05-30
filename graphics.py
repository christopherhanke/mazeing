from tkinter import Tk, BOTH, Canvas

class Window():
    def __init__(self, width, heigth):
        self.__root = Tk()
        self.__canvas = Canvas(height=heigth, width=width, bg="white")
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__visible = False
        self.__root.title("Mazeing")
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()
    
    def wait_for_close(self):
        self.__visible = True
        while self.__visible:
            self.redraw()
    
    def close(self):
        self.__visible = False
    
    def draw_line(self, line, color="black"):
        line.draw(self.__canvas, color)


class Point():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


class Line():
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2
    
    def draw(self, canvas, color):
        canvas.create_line(
            self.point1.x, self.point1.y,
            self.point2.x, self.point2.y,
            fill=color,
            width=2
        )


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
