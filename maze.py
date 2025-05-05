from time import sleep
from cell import *

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win

        self.create_cells()

    def create_cells(self):
        self.cells = []

        for i in range(self.num_cols):
            self.cells.append([])
            for j in range(self.num_rows):
                start_x = (i * self.cell_size_x) + self.x1
                start_y = (j * self.cell_size_y) + self.y1
                end_x = ((i + 1) * self.cell_size_x) + self.x1
                end_y = ((j + 1) * self.cell_size_y) + self.y1
                self.cells[-1].append(Cell(self.win, start_x, start_y, end_x, end_y))

                self.draw_cell(i, j)
    
    def draw_cell(self, i, j):
        self.cells[i][j].draw()
        self.animate()
        
    def animate(self):
        self.win.redraw()
        sleep(0.05)