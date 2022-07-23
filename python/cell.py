class Cell:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.north = None
        self.south = None
        self.east = None
        self.west = None
        self.links = {}
    def link(self, cell, bidi=True):
        self.links[cell] = True
        if bidi:
            cell.link(self, False)
    def unlink(self, cell, bidi=True):
        self.links.pop(cell)
        if bidi:
            cell.unlink(self, False)
    def get_links(self):
        return self.links.keys()
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