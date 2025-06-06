import unittest
from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0,0,num_rows,num_cols,10,10)
        self.assertEqual(len(m1.cells), num_cols)
        self.assertEqual(len(m1.cells[0]), num_rows)
    
    def test_maze_entrance_exit(self):
        num_cols = 10
        num_rows = 20
        m1 = Maze(0,0,num_rows,num_cols,10,10)
        self.assertFalse(m1.cells[0][0].has_top_wall)
        self.assertFalse(m1.cells[9][19].has_bottom_wall)
    
    def test_reset_visited(self):
        num_cols = 10
        num_rows = 20
        m1 = Maze(0,0,num_rows,num_cols,10,10)
        self.assertFalse(m1.cells[0][0].visited)
        self.assertFalse(m1.cells[9][19].visited)

if __name__ == "__main__":
    unittest.main()