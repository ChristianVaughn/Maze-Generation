from grid import ColoredGrid
from sidewinder import Sidewinder

grid = ColoredGrid(50, 50)
Sidewinder.on(grid)

start = grid[grid.rows//2, grid.columns//2]

grid.set_distances(start.distances())

img = grid.to_png()
img.show()