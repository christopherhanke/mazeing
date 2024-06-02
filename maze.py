import random

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
            win=None,
            seed=None
    ):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._cells = []
        if seed:
            random.seed(seed)
        
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)

    def _create_cells(self):
        for i in range(self._num_cols):
            row = []
            for j in range(self._num_rows):
                row.append(Cell(self._win))
            self._cells.append(row)
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)
                # self._cells[i][j] = self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        x1 = self._x1 + i * self._cell_size_x
        y1 = self._y1 + j *self._cell_size_y
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        
        if not self._win:
            return
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()

    def _animate(self):
        if not self._win:
            return
        self._win.redraw()
        sleep(0.05)
    
    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)

        self._cells[(self._num_cols - 1)][(self._num_rows - 1)].has_bottom_wall = False
        self._draw_cell(self._num_cols - 1, self._num_rows - 1)
    
    def _break_walls_r(self, i, j):
        self._cells[i][j]._visited = True
        while True:
            to_visit = []
            # top
            if j > 0:
                if not self._cells[i][j-1]._visited:
                    to_visit.append((i, j - 1))
            # bottom 
            if j < (self._num_rows - 1):
                if not self._cells[i][j + 1]._visited:
                    to_visit.append((i, j + 1))
            # left
            if i > 0:
                if not self._cells[i - 1][j]._visited:
                    to_visit.append((i - 1, j))
            # right
            if i < (self._num_cols - 1):
                if not self._cells[i + 1][j]._visited:
                    to_visit.append((i + 1, j))
            # break loop if empty
            if to_visit == []:
                self._draw_cell(i, j)
                self._animate()
                return
            # random direction
            k, l = to_visit[random.randrange(len(to_visit))]

            # self._cells[i][j] -> self._cells[k][l]
            # top
            if j - 1 == l:
                self._cells[i][j].has_top_wall = False
                self._cells[k][l].has_bottom_wall = False
            # bottom
            if j + 1 == l:
                self._cells[i][j].has_bottom_wall = False
                self._cells[k][l].has_top_wall = False
            # right
            if i + 1 == k:
                self._cells[i][j].has_right_wall = False
                self._cells[k][l].has_left_wall = False
            # left
            if i - 1 == k:
                self._cells[i][j].has_left_wall = False
                self._cells[k][l].has_right_wall = False
            
            # print(f"Cell: {i, j}, next {k, l}")
            self._break_walls_r(k, l)
        
