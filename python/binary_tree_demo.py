from grid import ColoredGrid
from binary_tree import BinaryTree

grid = ColoredGrid(20, 20)
BinaryTree.on(grid)

start = grid[grid.rows//2, grid.columns//2]
#start = grid[0, 0]

print(start)
grid.set_distances(start.distances())

deadends = grid.deadends()
print(len(deadends))
img = grid.to_png()
img.show()
