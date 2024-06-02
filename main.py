from graphics import Window
from maze import Maze


def main():
    screen_height = 600
    screen_width = 800
    num_rows = 10
    num_cols = 10
    margin = 20
    if screen_height < screen_width:
        cell_size = (screen_height - 2 * margin)
    else:
        cell_size = (screen_width - 2 * margin)
    if num_cols < num_rows:
        cell_size = cell_size // num_cols
    else:
        cell_size = cell_size // num_rows    
    
    win = Window(screen_width, screen_height)
    maze = Maze(margin, margin, num_rows, num_cols, cell_size, cell_size, win)
    print("maze created")
    is_solveable = maze.solve()
    if is_solveable:
        print("maze solved!")
    else:
        print("maze can not be solved!")
    win.wait_for_close()


main()
