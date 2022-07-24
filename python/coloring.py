from grid import ColoredGrid
from sidewinder import Sidewinder

grid = ColoredGrid(25, 25)
Sidewinder.on(grid)

start = grid[grid.rows//2, grid.columns//2]

grid.set_distances(start.distances())

img = grid.to_png()
img.show()
img.save('sidewinder.png')