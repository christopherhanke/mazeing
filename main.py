from graphics import Window
from cells import Cell


def main():
    win = Window(800, 600)

    c1 = Cell(0,0 , 50,50, win)
    c2 = Cell(50,0 , 100,50, win)
    c3 = Cell(0,50 , 50,100, win)
    c4 = Cell(50,50 , 100,100, win)
    
    c1.draw()
    c2.draw()
    c3.draw()
    c4.draw()

    c1.draw_move(c2)
    c2.draw_move(c4)

    win.wait_for_close()


main()
