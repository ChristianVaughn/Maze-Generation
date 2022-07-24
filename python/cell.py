from distances import Distances

class Cell:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.north = None
        self.south = None
        self.east = None
        self.west = None
        self.links = {}
        #self.distances = None

    def link(self, cell, bidi=True):
        self.links[cell] = True
        if bidi:
            cell.link(self, False)

    def unlink(self, cell, bidi=True):
        self.links.pop(cell)
        if bidi:
            cell.unlink(self, False)

    def get_links(self):
        return list(self.links.keys())

    def is_linked(self, cell):
        return cell in self.links

    def get_neighbors(self):
        neighbors = []
        if self.north:
            neighbors.append(self.north)
        if self.south:
            neighbors.append(self.south)
        if self.east:
            neighbors.append(self.east)
        if self.west:
            neighbors.append(self.west)
        return neighbors
    
    def distances(self):
        distances = Distances(self)
        frontier = [self]
        while len(frontier) > 0:
            new_frontier = []
            for cell in frontier: 
                for linked in cell.get_links():
                    #! Might not work. Possible replacement: if self.distances[linked]
                    if linked in distances: 
                        continue
                    distances[linked] = distances[cell] + 1
                    new_frontier.append(linked)
            frontier = new_frontier
        return distances