import random

class BinaryTree:
    @staticmethod
    def on(grid):
        for cell in grid.each_cell():
            
            neighbors = []
            if(cell.north):
                neighbors.append(cell.north)
            if(cell.east):
                neighbors.append(cell.east)
            neighbor = random.choice(neighbors) if len(neighbors) > 0 else None
            if(neighbor):
                cell.link(neighbor)            