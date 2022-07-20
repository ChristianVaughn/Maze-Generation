#include "cell.cc"
#include <vector>
#include "generator.cc"

class Grid {
    
    private:
        int rows, cols;
        std::vector<std::vector<Cell*>> grid;
    public:
        Grid(int rows_, int cols_) {
            rows = rows_;
            cols = cols_;
            grid = init_grid();
            config_cells();

        }
        std::vector<std::vector<Cell*>> init_grid() {
            for (int i = 0; i < rows; i++) {
                std::vector<Cell*> row;
                for (int j = 0; j < cols; j++) {
                    row.push_back(new Cell(i, j));
                }
                grid.push_back(row);
            }
            return grid;
        }
        void config_cells() {
            for (int i = 0; i < rows; i++) {
                for (int j = 0; j < cols; j++) {
                    Cell* cell = grid[i][j];
                    cell -> north = (i > 0) ? grid[i - 1][j] : nullptr;
                    cell -> south = (i < rows - 1) ? grid[i + 1][j] : nullptr;
                    cell -> east = (j < cols - 1) ? grid[i][j + 1] : nullptr;
                    cell -> west = (j > 0) ? grid[i][j - 1] : nullptr;
                }
            }
        }
    Cell* operator[](std::pair<int, int> pos) {
        //if first pos is out of bounds, return nullptr
        if (pos.first < 0 || pos.first >= rows)
            return nullptr;
        //if second pos is out of bounds, return nullptr
        if (pos.second < 0 || pos.second >= cols)
            return nullptr;
        //otherwise return the cell at the given position
        return grid[pos.first][pos.second];
    }
    Cell* random_cell() {
        int row = rand() % rows;
        int col = rand() % cols;
        return grid[row][col];
    }
    int get_size() {
        return rows * cols;
    }
    Generator<std::vector <Cell*>> each_row() {
        for(auto const& row : grid)
            co_yield row;
    }
    Generator<Cell*> each_cell() {

        for(auto const& row : each_row()) {
            for(auto const& cell : row)
                co_yield cell;
               break; 
        }
    }
};
