from grid import DistanceGrid
from sidewinder import Sidewinder

grid = DistanceGrid(50, 50)
Sidewinder.on(grid)

start = grid[0, 0]

distances = start.distances()
new_start, distance = distances.max()

new_distances = new_start.distances()
goal, distance = new_distances.max()

grid.distances = new_distances.path_to(goal)
#print(grid)
img = grid.to_png()
img.show()