from grid import Grid
from sidewinder import Sidewinder

grid = Grid(5, 5)
Sidewinder.on(grid)
print(grid)
img = grid.to_png()
img.show()
#img.save('sidewinder.png')