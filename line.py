from __future__ import annotations
from typing import TYPE_CHECKING


class Line:
    def __init__(self, start: Point, end: Point):
        self.start = start
        self.end = end

    def draw(self, canvas: Canvas, fill_color: str):
        canvas.create_line(
            self.start.x, self.start.y, self.end.x, self.end.y, fill=fill_color, width=2
        )


if TYPE_CHECKING:
    from tkinter import Canvas
    from point import Point
