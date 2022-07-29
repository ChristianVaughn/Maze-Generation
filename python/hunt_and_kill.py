import random

class HuntAndKill:
    @staticmethod
    def on(grid):

        current = grid.random_cell()
        while current:
            unvisited_neighbor = [n for n in current.get_neighbors() if not n.get_links()]

            if unvisited_neighbor:
                neighbor = random.choice(unvisited_neighbor)
                current.link(neighbor)
                current = neighbor
            else:
                current = None

                for cell in grid.each_cell():
                    visited_neighbor = [n for n in cell.get_neighbors() if n.get_links()]
                    
                    if not cell.get_links() and visited_neighbor:
                        current = cell

                        neighbor = random.choice(visited_neighbor)
                        current.link(neighbor)
                        break