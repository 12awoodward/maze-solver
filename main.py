from window import *
from point import *
from line import *

def main():
    win = Window(800, 600)

    top_left = Point(10,10)
    top_right = Point(100,10)
    bot_left = Point(10,100)
    bot_right = Point(100,100)

    top = Line(top_left, top_right)
    left = Line(top_left, bot_left)
    right = Line(top_right, bot_right)
    bottom = Line(bot_left, bot_right)

    win.draw_line(top, "black")
    win.draw_line(left, "red")
    win.draw_line(right, "blue")
    win.draw_line(bottom, "green")

    win.wait_for_close()

main()