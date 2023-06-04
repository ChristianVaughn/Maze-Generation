from recursive_backtracker import RecursiveBacktracker
from grid import Grid

grid = Grid(20,20)
RecursiveBacktracker.on(grid)

img = grid.to_png()
img.show()
