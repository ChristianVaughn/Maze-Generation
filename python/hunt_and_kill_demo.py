from hunt_and_kill import HuntAndKill
from grid import ColoredGrid

grid = ColoredGrid(20, 20)
HuntAndKill.on(grid)

start = grid[grid.rows//2, grid.columns//2]
#start = grid[0, 0]


grid.set_distances(start.distances())

img = grid.to_png()
img.show()