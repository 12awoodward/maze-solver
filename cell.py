from __future__ import annotations
from typing import TYPE_CHECKING

from point import Point
from line import Line


class Cell:
    def __init__(
        self, x1: float, y1: float, x2: float, y2: float, window: Window | None = None
    ):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True

        self.top_left = Point(x1, y1)
        self.top_right = Point(x2, y1)
        self.bottom_left = Point(x1, y2)
        self.bottom_right = Point(x2, y2)

        self.win = window
        self.visited = False

    def draw(self):
        if not self.win:
            return

        colors = ("#d9d9d9", "black")

        left = Line(self.top_left, self.bottom_left)
        right = Line(self.top_right, self.bottom_right)
        top = Line(self.top_left, self.top_right)
        bottom = Line(self.bottom_left, self.bottom_right)

        self.win.draw_line(left, colors[self.has_left_wall])
        self.win.draw_line(right, colors[self.has_right_wall])
        self.win.draw_line(top, colors[self.has_top_wall])
        self.win.draw_line(bottom, colors[self.has_bottom_wall])

    def get_midpoint(self):
        x = (self.top_left.x + self.bottom_right.x) / 2
        y = (self.top_left.y + self.bottom_right.y) / 2
        return Point(x, y)

    def draw_move(self, to_cell: Cell, undo: bool = False):
        if not self.win:
            return

        color = "red"
        if undo:
            color = "#a9a9a9"

        move = Line(self.get_midpoint(), to_cell.get_midpoint())
        self.win.draw_line(move, color)


if TYPE_CHECKING:
    from window import Window
