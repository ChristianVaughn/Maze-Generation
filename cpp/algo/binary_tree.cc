// #include"../grid.cc"
// #include<vector>
#include <random>

class BinaryTree{
    public:
     static void on(Grid grid){
        std::random_device dev;
        std::mt19937 rng(dev());
        for(auto const& cell : grid.each_cell()) {
            std::vector<Cell*> neighbors;
            if (cell -> north)
                neighbors.push_back(cell -> north);
            if (cell -> east)
                neighbors.push_back(cell -> east);

            std::uniform_int_distribution<std::mt19937::result_type> dist(0,neighbors.size()-1);
            int index = dist(rng);
            if (neighbors.size())
                cell -> link(neighbors.at(index));
        }
     }
};