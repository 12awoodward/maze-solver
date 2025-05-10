from time import sleep
from cell import *

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win = None):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win

        self.create_cells()
        self.break_entrance_and_exit()

    def create_cells(self):
        self.cells = []

        for i in range(self.num_cols):
            self.cells.append([])
            for j in range(self.num_rows):
                start_x = (i * self.cell_size_x) + self.x1
                start_y = (j * self.cell_size_y) + self.y1
                end_x = ((i + 1) * self.cell_size_x) + self.x1
                end_y = ((j + 1) * self.cell_size_y) + self.y1
                self.cells[-1].append(Cell(start_x, start_y, end_x, end_y, self.win))

                self.draw_cell(i, j)
    
    def draw_cell(self, i, j):
        if not self.win:
            return
        
        self.cells[i][j].draw()
        self.animate()
        
    def animate(self):
        self.win.redraw()
        sleep(0.05)
    
    def break_entrance_and_exit(self):
        self.cells[0][0].has_top_wall = False
        self.draw_cell(0, 0)

        last_col = self.num_cols - 1
        last_row = self.num_rows - 1
        self.cells[last_col][last_row].has_bottom_wall = False
        self.draw_cell(last_col, last_row)
