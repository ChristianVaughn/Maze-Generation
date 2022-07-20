#include"../grid.cc"
#include<vector>
class BinaryTree{
    public:
     void on(Grid grid){
        for(auto const& cell : grid.each_cell()) {
            std::vector<Cell*> neighbors;
            if (cell -> north)
                neighbors.push_back(cell -> north);
            if (cell -> east)
                neighbors.push_back(cell -> east);
            int index = rand() % neighbors.size();
            if (neighbors[index])
                cell -> link(neighbors[index]);
        }
     }
};