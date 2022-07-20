#include<iostream>
#include"grid.cc"
#include"algo/binary_tree.cc"

int main() {
    Grid grid(7, 7);
    
    BinaryTree::on(grid);
    grid.print();

    return 0;
}