from grid import ColoredGrid
from wilsons import Wilsons

for n in range(4):
    grid = ColoredGrid(20, 20)
    Wilsons.on(grid)
    middle = grid[grid.rows // 2, grid.columns // 2]
    grid.set_distances(middle.distances())
    img = grid.to_png()
    img.save("./images/wilson_colored_%d.png" % n)