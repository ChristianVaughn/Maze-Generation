from grid import DistanceGrid
from binary_tree import BinaryTree

grid = DistanceGrid(5, 5)
BinaryTree.on(grid)

start = grid[0, 0]
distances = start.distances()

grid.distances = distances
print(grid)

print("Path from NW corner to SW corner:")
grid.distances = distances.path_to(grid[grid.rows - 1, 0])
print(grid)