import random
from cell import Cell
from PIL import Image, ImageDraw, ImageColor
from numpy import base_repr


class Grid:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.grid = self.init_grid(rows, columns)
        self.config_cells()

    def init_grid(self, rows, columns):
        grid = []
        for row in range(rows):
            grid.append([])
            for column in range(columns):
                grid[row].append(Cell(row, column))
        return grid

    def config_cells(self):
        for row in range(self.rows):
            for column in range(self.columns):
                cell = self.grid[row][column]
                if row > 0:
                    cell.north = self.grid[row-1][column]
                if row < self.rows-1:
                    cell.south = self.grid[row+1][column]
                if column > 0:
                    cell.west = self.grid[row][column-1]
                if column < self.columns-1:
                    cell.east = self.grid[row][column+1]

    #overload the [] operator to return the cell at a given row and column
    def __getitem__(self, index):
        #if index is a tuple, return the cell at the given row and column
        if type(index) is tuple:
            #if the row is out of bounds, return None
            if index[0] < 0 or index[0] >= self.rows:
                return None
            #if the column is out of bounds, return None
            if index[1] < 0 or index[1] >= self.columns:
                return None
            return self.grid[index[0]][index[1]]
        #otherwise return null
        return None
        
    #return a random cell
    def random_cell(self):
        row = random.randint(0, self.rows-1)
        column = random.randint(0, self.columns-1)
        return self.grid[row][column]

    #get size of the grid
    def size(self):
        return self.rows * self.columns

    #loop each row and yield the row
    def each_row(self):
        for row in self.grid:
            yield row

    #loop each cell and yield the cell
    def each_cell(self):
        for row in self.each_row():
            for cell in row:
                yield cell

    def contents_of(self, cell):
        return " "

    #overwrite the str operator to return the grid as a string
    def __str__(self):
        output = "+"
        for column in range(self.columns):
            output += "---+"
        output += "\n"
        for row in self.grid:
            top = "|"
            bottom = "+"
            for cell in row:
                #if cell is none create a new cell at -1,-1
                if cell is None:
                    cell = Cell(-1,-1)
                body = " " + self.contents_of(cell) + " "
                east_wall = " " if cell.is_linked(cell.east) else "|"
                top += body + east_wall
                south_wall = "   " if cell.is_linked(cell.south) else "---"
                corner = "+"
                bottom += south_wall + corner
            output += top + "\n" + bottom + "\n"
        return output

    def background_color_for(self, cell):
        return None

    def to_png(self,cell_size = 10):
        img_width = cell_size * self.columns
        img_height = cell_size * self.rows
        img = Image.new('RGB', (img_width+1, img_height+1), color = 'white')
        draw = ImageDraw.Draw(img)
        for mode in ["background", "walls"]:
            for cell in self.each_cell():
                x1 = cell.col * cell_size
                y1 = cell.row * cell_size
                x2 = (cell.col + 1) * cell_size
                y2 = (cell.row + 1) * cell_size

                if mode == "background":
                    color = self.background_color_for(cell)
                    if color is not None:
                        draw.rectangle((x1, y1, x2, y2), fill = color)
                else:
                    if not cell.north:
                        draw.line((x1, y1, x2, y1), fill = 'black')
                    if not cell.west:
                        draw.line((x1, y1, x1, y2), fill = 'black')

                    if not cell.is_linked(cell.east):
                        draw.line((x2, y1, x2, y2), fill = 'black')
                    if not cell.is_linked(cell.south):
                        draw.line((x1, y2, x2, y2), fill = 'black')
        return img

#DistanceGrid class that inherits from Grid
class DistanceGrid(Grid):
    def __init__(self, rows, columns):
        super().__init__(rows, columns)
        self.distances = None

    #override the contents_of method to return the distance of the cell
    def contents_of(self, cell):
        if self.distances and cell in self.distances:
            return base_repr(self.distances[cell], base = 36)
        else:
            return super().contents_of(cell)
    
    #! NOT Proper way to do this. Only works if distances contains longest path
    #TODO find a better way to do this i.e. to color the longest path
    def background_color_for(self, cell):
        if self.distances and cell in self.distances:
                return 'green'
        else:
            return None

class ColoredGrid(Grid):
    def __init__(self, rows, columns):
        super().__init__(rows, columns)
        self.distances = None
        self.max = None

    def set_distances(self,distances):
        self.distances = distances
        farthest, self.max = distances.max()

    def background_color_for(self, cell):
        distance = self.distances[cell] 
        if not distance:
            return None
        intensity = (self.max - distance) / self.max
        dark = int(intensity * 255)
        bright = 128 + int(intensity * 127)
        return (dark, bright, dark)