from graphics import Window, Cell


def main():
    win = Window(800, 600)

    Cell(0,0 , 100,100, win).draw()
    Cell(10,10 , 50,50, win).draw()

    win.wait_for_close()


main()
