from time import sleep
from cell import *
import random

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win = None, seed = None):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win

        if seed:
            random.seed(seed)

        self.create_cells()
        self.break_entrance_and_exit()
        self.break_walls_r(0, 0)
        self.reset_cells_visited()
        self.solve()

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
    
    def break_walls_r(self, i, j):
        self.cells[i][j].visited = True
        moves = [(0,-1), (1,0), (0,1),(-1,0)]

        while True:
            possible_paths = []

            for move in moves:
                result = (i + move[0], j + move[1])
                if result[0] >= 0 and result[0] < self.num_cols and result[1] >= 0 and result[1] < self.num_rows:
                    if not self.cells[result[0]][result[1]].visited:
                        possible_paths.append(move)

            if not possible_paths:
                self.draw_cell(i, j)
                return
            
            chosen = random.choice(possible_paths)
            new_coords = (i + chosen[0], j + chosen[1])
            new_cell = self.cells[new_coords[0]][new_coords[1]]
            current_cell = self.cells[i][j]

            match chosen:
                case (0,-1):
                    current_cell.has_top_wall = False
                    new_cell.has_bottom_wall  = False
                case (1,0):
                    current_cell.has_right_wall = False
                    new_cell.has_left_wall  = False
                case (0,1):
                    current_cell.has_bottom_wall = False
                    new_cell.has_top_wall  = False
                case (-1,0):
                    current_cell.has_left_wall = False
                    new_cell.has_right_wall  = False

            self.break_walls_r(new_coords[0], new_coords[1])

    def reset_cells_visited(self):
        for col in self.cells:
            for cell in col:
                cell.visited = False
    
    def solve(self):
        return self.solve_r(0, 0)

    def solve_r(self, i, j):
        self.animate()
        current_cell = self.cells[i][j]
        current_cell.visited = True

        if i == self.num_cols - 1 and j == self.num_rows - 1:
            return True
        
        moves = [(0, -1, current_cell.has_top_wall), (1, 0, current_cell.has_right_wall), (0, 1, current_cell.has_bottom_wall), (-1, 0, current_cell.has_left_wall)]

        for move in moves:
            new_coord = (i + move[0], j + move[1])

            if new_coord[0] >= 0 and new_coord[0] < self.num_cols and new_coord[1] >= 0 and new_coord[1] < self.num_rows:
                new_cell = self.cells[new_coord[0]][new_coord[1]]

                if not (move[2] or new_cell.visited):
                    current_cell.draw_move(new_cell)

                    if self.solve_r(new_coord[0], new_coord[1]):
                        return True
                    current_cell.draw_move(new_cell, True)
        
        return False
