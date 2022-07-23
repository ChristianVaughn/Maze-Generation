import random
from cell import Cell

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
                body = "   "
                east_wall = (cell.is_linked(cell.east) ? " " : "|")
                top += body + east_wall
                south_wall = (cell.is_linked(cell.south) ? "   " : "---")
                corner = "+"
                bottom += south_wall + corner
            output += top + "\n" + bottom + "\n"
        return output
        