import random

class AldousBroder:
    @staticmethod
    def on(grid):

        cell = grid.random_cell()
        unvisited = grid.size() - 1

        while unvisited > 0:
            neighbor = random.choice(cell.get_neighbors())
            if not neighbor.get_links():
                cell.link(neighbor)
                unvisited -= 1
            cell = neighbor
        