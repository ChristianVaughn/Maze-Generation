from grid import ColoredGrid
from aldous_broder import AldousBroder

grid = ColoredGrid(20, 20)
AldousBroder.on(grid)
middle = grid[grid.rows // 2, grid.columns // 2]
grid.set_distances(middle.distances())
img = grid.to_png()
img.show()