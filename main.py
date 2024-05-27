from tkinter import Tk, BOTH, Canvas

class Window():
    def __init__(self, width, heigth):
        self.__root = Tk()
        self.__canvas = Canvas(height=heigth, width=width, bg="black")
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

def main():
    win = Window(800, 600)
    win.wait_for_close()


main()
