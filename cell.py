from point import *
from line import *

class Cell:
    def __init__(self, x1, y1, x2, y2, window = None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True

        self.top_left = Point(x1, y1)
        self.top_right = Point(x2, y1)
        self.bottom_left = Point(x1, y2)
        self.bottom_right = Point(x2, y2)

        self.win = window

    def draw(self):
        color = "black"
        if self.has_left_wall:
            left = Line(self.top_left, self.bottom_left)
            self.win.draw_line(left, color)
        if self.has_right_wall:
            right = Line(self.top_right, self.bottom_right)
            self.win.draw_line(right, color)
        if self.has_top_wall:
            top = Line(self.top_left, self.top_right)
            self.win.draw_line(top, color)
        if self.has_bottom_wall:
            bottom = Line(self.bottom_left, self.bottom_right)
            self.win.draw_line(bottom, color)

    def get_midpoint(self):
        x = (self.top_left.x + self.bottom_right.x) / 2
        y = (self.top_left.y + self.bottom_right.y) / 2
        return Point(x, y)
    
    def draw_move(self, to_cell, undo=False):
        color = "red"
        if undo:
            color = "gray"
        
        move = Line(self.get_midpoint(), to_cell.get_midpoint())
        self.win.draw_line(move, color)