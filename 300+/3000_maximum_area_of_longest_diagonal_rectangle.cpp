

/*
3000. Maximum Area of Longest Diagonal Rectangle (https://leetcode.com/problems/maximum-area-of-longest-diagonal-rectangle/description/?envType=daily-question&envId=2025-08-26)w


getting the longest diagonal
    use pythagorean theorem on each rectangle length and width to get the diagonal length

two cases:
1. current rectangle has a larger diagonal than the largest diagonal seen so far
    simply update the new largest diagonal value and the corresponding area of that rectangle

2. current rectangle has an equal diagonal to the largest diagonal seen so far
    since the diagonals are equal, need to check whether or not the current area is larger than the area of the largest diagonal rectangle
    simply just check if (currDiag == largestDiag && currArea > largestArea)

runtime: O(n) where n is the size of dimensions
space: O(1)
*/


#include <iostream>
#include <vector>
using namespace std;


double getDiagonal(int n, int m) {
    return sqrt(n*n + m*m);
}

int areaOfMaxDiagonal(vector<vector<int>>& dimensions) {
    double largestDiag = 0;
    int largestArea = 0; // area of the rectangle with largest diagonal

    for (vector<int>& rectangle : dimensions) {
        double currDiag = getDiagonal(rectangle[0], rectangle[1]); 
        int currArea = rectangle[0] * rectangle[1];

        if (currDiag == largestDiag && currArea > largestArea) {
            largestArea = currArea;
        } else if (currDiag > largestDiag) {
            largestArea = currArea;
            largestDiag = currDiag;
        }
    }

    return largestArea;
}

int main() {

    vector<vector<int>> dimensions = {{9, 3}, {8, 6}};
    cout << areaOfMaxDiagonal(dimensions) << endl;
    return 0;
}