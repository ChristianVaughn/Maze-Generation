import random

class RecursiveBacktracker:
    @staticmethod
    def on(grid, start_at = None):
        if start_at is None:
            start_at = grid.random_cell()

        stack = []
        stack.append(start_at)
        
        while stack:
            current = stack[-1]
            neighbors = [n for n in current.get_neighbors() if not n.get_links()]
            
            if not neighbors:
                stack.pop()
            else:
                neighbor = random.choice(neighbors)
                current.link(neighbor)
                stack.append(neighbor)
