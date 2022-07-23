#include<iostream>
#include"grid.cc"
#include"algo/binary_tree.cc"
#include"algo/sidewinder.cc"


int main() {
    Grid grid(7, 7);
    
    Sidewinder::on(grid);
    grid.print();

    return 0;
}