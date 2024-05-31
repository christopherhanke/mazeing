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


