#include <random>
#include<vector>

class Sidewinder{
    public:
     static void on(Grid grid){
        std::random_device dev;
        std::mt19937 rng(dev());
        std::uniform_int_distribution<std::mt19937::result_type> dist(0,1);
        for(auto const& row : grid.each_row()) {
            std::vector<Cell*> run;

            for(auto const& cell : row) {
                run.push_back(cell);

                bool is_east_bound = (cell -> east == nullptr);
                bool is_north_bound = (cell -> north == nullptr);
                
                bool should_close_out = is_east_bound || (!is_north_bound && dist(rng) == 0);
                
                if (should_close_out) {
                    std::uniform_int_distribution<std::mt19937::result_type> dst(0,run.size()-1);
                    Cell* member = run.at(dst(rng));
                    if (member -> north != nullptr)
                        member -> link(member -> north);
                    run.clear();
                }
                else {
                    cell -> link(cell -> east);
                }

            }
        }

     }
};