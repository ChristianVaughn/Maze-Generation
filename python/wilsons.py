import random

class Wilsons:
    @staticmethod
    def on(grid):
        unvisited = []
        for cell in grid.each_cell():
            unvisited.append(cell)

        first = random.choice(unvisited)
        unvisited.remove(first)        
        #loop while unvisited is not empty
        while unvisited:
            cell = random.choice(unvisited)
            path = [cell]

            #while cell is in the unvisited list
            while cell in unvisited:
                cell = random.choice(cell.get_neighbors())
                position = path.index(cell) if cell in path else -1
                if position != -1:
                    #remove the path from the end of the list to the cell
                    path = path[0:position+1]
                else:
                    #add the cell to the end of the path
                    path.append(cell)
            for index in range(len(path) - 1):
                path[index].link(path[index + 1])
                unvisited.remove(path[index])
            path = []
            
