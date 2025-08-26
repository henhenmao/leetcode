

/*
3195. Find the Minimum Area to Cover All Ones I (https://leetcode.com/problems/find-the-minimum-area-to-cover-all-ones-i/?envType=daily-question&envId=2025-08-26)

getting minimum area:
    find the row index of the topmost 1
    find the row index of the bottommost 1
    find the column index of the leftmost 1
    find the column index of the rightmost 1

    bottommost - topmost = height of smallest rectangle
    rightmost - leftmost = length of smallest rectangle

algorithm:
    1. do a traversal of the entire matrix
    2. update the important indexes along the way
        update the topmost and bottommost row that contains a 1
        update the leftmost and rightmost column that contains a 1
    3. calculate the dimensions of the smallest rectangle
        bottommost - topmost + 1 = height of smallest rectangle
        rightmost - leftmost + 1 = length of smallest rectangle
    4. area = length * height

runtime: O(n * m) where n and m are the dimensions of the matrix
space: O(1)
*/

#include <iostream>
#include <vector>
using namespace std;

int minimumArea(vector<vector<int>>& grid) {
    int n = grid.size(), m = grid[0].size();
    int topmost = n, bottommost = 0, leftmost = m, rightmost = 0;

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (grid[i][j] == 1) {
                topmost = min(topmost, i);
                bottommost = max(bottommost, i);
                leftmost = min(leftmost, j);
                rightmost = max(rightmost, j);
            }
        }
    }

    int height = bottommost - topmost + 1;
    int length = rightmost - leftmost + 1;
    return length * height;
}

int main() {

    vector<vector<int>> grid = {{0,1,0},{1,0,1}};

    cout << minimumArea(grid) << endl;

    return 0;
}

