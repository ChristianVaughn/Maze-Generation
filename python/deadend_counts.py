from grid import Grid
from binary_tree import BinaryTree
from sidewinder import Sidewinder
from aldous_broder import AldousBroder
from wilsons import Wilsons
from hunt_and_kill import HuntAndKill
from statistics import fmean

algorithms = [BinaryTree, Sidewinder, AldousBroder, Wilsons, HuntAndKill]

tries = 100
size = 20

averages = {}

for algorithm in algorithms: 
    print("running ", algorithm.__name__)

    deadend_counts = []
    for _ in range(tries):
        grid = Grid(size, size)
        algorithm.on(grid)
        deadend_counts.append(len(grid.deadends()))
    averages[algorithm] = fmean(deadend_counts)

total_cells = size*size
print()
print(f"Avearage dead-ends per {size}x{size} maze ({total_cells}):")
print()

sorted_algorithms = sorted(algorithms, key = lambda algorithm: averages[algorithm])

for algorithm in sorted_algorithms:
    percentage = averages[algorithm] * 100.0 / (size * size)
    print(f"{algorithm.__name__}: {round(averages[algorithm])}/{total_cells} ({percentage}%)")
