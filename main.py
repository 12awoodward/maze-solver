from window import *
from point import *
from line import *
from cell import *

def main():
    win = Window(800, 600)

    box = Cell(win, 2, 2, 100, 100)
    box.draw()
    box1 = Cell(win, 100, 2, 200, 100)
    box1.draw()
    box2 = Cell(win, 125, 125, 550, 550)
    box2.draw()
    box3 = Cell(win, 2, 100, 100, 200)
    box3.draw()

    box.draw_move(box1)
    box.draw_move(box3, True)
    box1.draw_move(box3)

    win.wait_for_close()

main()