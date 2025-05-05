from window import *
from point import *
from line import *
from cell import *
from maze import *

def main():
    win = Window(800, 600)

    maze = Maze(50, 25, 5, 8, 100, 100, win)

    win.wait_for_close()

main()