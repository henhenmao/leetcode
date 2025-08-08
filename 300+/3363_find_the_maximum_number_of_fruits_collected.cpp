

/*
3363. Find the Maximum Number of Fruits Collected (https://leetcode.com/problems/find-the-maximum-number-of-fruits-collected/description/?envType=daily-question&envId=2025-08-07)

child 1 = top left child at (0,0)
child 2 = top right child at (0, n-1)
child 3 = bottom left child at (n-1, 0)

the fact that each child must make (n-1) moves to reach room (n-1, n-1) makes life much much easier

child 1
    has only one single path
    since the shortest path from (0,0) to (n-1,n-1) is a straight line diagonally down, with a distance of (n-1)
        this is the only path that child 1 can take 

child 2
    to ensure that child 2 makes to the end in n-1 moves, it must go down a row each move
    it also cannot cross beyond left of column (n/2), as it will not be able turn right to make it to (n-1, n-1)

child 3
    to ensure that child 3 makes to the end in n-1 moves, it must go right a column each move
    it also cannot cross above row (n/2), as it will not be able turn down to make it to (n-1, n-1)

i'm going to assume that child 2 or 3 will never have to cross or go on the path of child 1 as that would be not optimal
this is a diagram of each child's "territory" on a 5x5 grid and a 6x6 grid

    1 0 0 0 2           1 0 0 0 0 2
    0 1 0 2 2           0 1 0 0 2 2
    0 0 1 2 2           0 0 1 2 2 2
    0 3 3 1 2           0 0 3 1 2 2 
    3 3 3 3 #           0 3 3 3 1 2
                        3 3 3 3 3 #

we just need to make sure that child 2 or 3 never go on 1's path, while adhering to their movement rules
    also add some dp to maximize the number of fruits collected by each child

each child has like a litte triangle territory thing going on for them
    since they probably won't interfere with each other, just do two separate maximum path dp's on childs 2 and 3
    add the maximum path sums from both children and add the diagonal line form child 1 to get the max sum

algorithm:
    1. count the path sum from child 1 and set all cells in the path to 0 (fruit is collected)
    2. do some goofy math to set all redundant cells to 0
        redundant cells are the cells that are not a part of either child 2 or child 3's path territory
        avoids including redundant cells in the path sums.
    3. do some more goofy math to traverse in a triangle shape for child 2 and child 3
        any values of grid[i][j] for a child can be mirrored for the other child by accessing grid[j][i]
        for each cell of child 2, add to grid[i][j] the max of the three previous cells in the row above
            grid[i-1][j-1], grid[i-1][j], grid[i-1][j+1]
        for each cell of child 3, add to grid[i][j] the max of the three previous cells int he left column
            grid[i-1][j-1], grid[i][j-1], grid[i+1][j-1]
    4. the last cells of each triangle at grid[n-1][n-2] and grid[n-2][n-1] contain the max path sums of each child
        add both to the diagonal sum fromt he first child to get the max sum
*/

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int maxCollectedFruits(vector<vector<int>>& grid) {
    int total = 0;
    int n = grid.size();    

    // child 1 path
    for (int i = 0; i < n; i++) {
        total += grid[i][i];
        grid[i][i] = 0;
    }

    // filling zeros in redundant cells that will not be in any path
    for(int i = 0; i < n-2; i++){
            grid[i][n-2-i] = grid[i][n-3-i]=0;
        }
        grid[n-2][0] = 0;
    
    // child 2 and 3
    for (int i = 1; i < n-1; i++) {
        for (int j = max(i+1, n-i-1); j < n-1; j++) {
            grid[i][j] += max(grid[i-1][j], max(grid[i-1][j-1], grid[i-1][j+1]));
            grid[j][i] += max(grid[j][i-1], max(grid[j-1][i-1], grid[j+1][i-1]));
        }
        grid[i][n-1] += max(grid[i-1][n-2], grid[i-1][n-1]);
        grid[n-1][i] += max(grid[n-2][i-1], grid[n-1][i-1]);
    }

    total += grid[n-2][n-1];
    total += grid[n-1][n-2];


    // REMEMBER TO COMMENT OUT OR DELETE PRINT STATEMENTS IN SUBMISSIONS SO IT DOESN'T TLE
    // REMEMBER TO COMMENT OUT OR DELETE PRINT STATEMENTS IN SUBMISSIONS SO IT DOESN'T TLE
    // REMEMBER TO COMMENT OUT OR DELETE PRINT STATEMENTS IN SUBMISSIONS SO IT DOESN'T TLE
    // REMEMBER TO COMMENT OUT OR DELETE PRINT STATEMENTS IN SUBMISSIONS SO IT DOESN'T TLE
    // REMEMBER TO COMMENT OUT OR DELETE PRINT STATEMENTS IN SUBMISSIONS SO IT DOESN'T TLE

    // for (vector<int> row : grid) {
    //     for (int fruit : row) {
    //         cout << fruit << " ";
    //     }
    //     cout << endl;
    // }
    
    return total;
}

int main() {
    vector<vector<int>> fruits = {{1,2,3,4}, {5,6,8,7}, {9,10,11,12}, {13,14,15,16}};
    cout << maxCollectedFruits(fruits) << endl;
    return 0;
}