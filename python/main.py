from grid import Grid
from sidewinder import Sidewinder

grid = Grid(25, 25)
Sidewinder.on(grid)
#print(grid)
img = grid.to_png()
img.save('sidewinder.png')