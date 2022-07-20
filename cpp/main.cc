#include<iostream>
#include"grid.cc"
#include"algo/binary_tree.cc"

int main() {
    Grid grid(10, 10);
    std::cout << grid.get_size() << std::endl;
    return 0;
}