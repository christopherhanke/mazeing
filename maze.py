from cells import Cell
from time import sleep

class Maze():
    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            win=None
    ):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._cells = []
        self._create_cells()

    def _create_cells(self):
        for i in range(self._num_cols):
            row = []
            for j in range(self._num_rows):
                row.append(None)
            self._cells.append(row)
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._cells[i][j] = self._draw_cell(i, j)
        
        self._break_entrance_and_exit()
        

    def _draw_cell(self, i, j):
        x1 = self._x1 + i * self._cell_size_x
        y1 = self._y1 + j *self._cell_size_y
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        cell = Cell(x1, y1, x2, y2, self._win)
        if not self._win:
            return cell
        """
        if i == 0 and j == 0:
            cell.has_top_wall = False
        if i == (self._num_cols - 1) and j == (self._num_rows - 1):
            cell.has_bottom_wall = False
        """
        cell.draw()
        self._animate()
        return cell

    def _animate(self):
        self._win.redraw()
        sleep(0.05)
    
    def _break_entrance_and_exit(self):
        entrance = self._cells[0][0]
        entrance.has_top_wall = False
        entrance.draw()
        self._animate()

        exit = self._cells[(self._num_cols - 1)][(self._num_rows - 1)]
        exit.has_bottom_wall = False
        exit.draw()
        self._animate()
        
