
#include <map>
#include <vector>

class Cell {
    
    //should make this private but too lazy to make a getter/setter for each
    public:
        int row, col;
        Cell* north;
        Cell* south;
        Cell* east;
        Cell* west;
        std::map<Cell*,bool> links;
    //public:

        Cell(int row_, int col_) {
            row = row_;
            col = col_;
        }
        
        void link(Cell* cell, bool bidi=true){
            links[cell] = true;
            if (bidi)
                cell -> link(this, false);
        }
        void unlink(Cell* cell, bool bidi = true) {
            links.erase(cell);
            if (bidi)
                cell -> unlink(this, false);
        }
        std::vector<Cell*> get_links(){
            std::vector<Cell*> vec;
            for(auto const& val : links)
                vec.push_back(val.first);
            return vec;
        }
        bool is_linked(Cell* cell){
            return links.contains(cell);
        }
        std:: vector<Cell*> get_neighbors(){
            std::vector<Cell*> vec;

            if (north != nullptr)
                vec.push_back(north);
            if(south != nullptr)
                vec.push_back(south);
            if(east != nullptr)
                vec.push_back(east);
            if(west != nullptr)
                vec.push_back(west);
            return vec;

        }
};
