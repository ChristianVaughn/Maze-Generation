from grid import Grid
from aldous_broder import AldousBroder

grid = Grid(20, 20)
AldousBroder.on(grid)

img = grid.to_png()
img.show()

