from graphics import Window
from maze import Maze


def main():
    win = Window(800, 600)
    maze = Maze(10, 10, 6, 6, 50, 50, win, seed=0)

    win.wait_for_close()


main()
