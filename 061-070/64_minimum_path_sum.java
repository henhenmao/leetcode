
/*
64. Minimum Path Sum (https://leetcode.com/problems/minimum-path-sum/description/)

we must use tabulation for this problem

algorithm:
    1. create a n x m dp table and set dp[0][0] to grid[0][0]
    2. do a double loop to traverse each cell in the grid
    3. for each cell, check the cell on top and the cell to the left of it
        this is essentially checking the possibility of moving right and moving down in the question
        the cell on top and to the left represent the minimum path for that particular cell
    4. choose the smaller of the top and left and add the current path sum (grid[i][j]) to it
    5. at the end, dp[n-1][m-1] will contain the minimum path sum to [0][0] 

runtime: O(n * m)
space: O(n * m)

*/

class Solution {
    public int minPathSum(int[][] grid) {
        int n = grid.length;
        int m = grid[0].length;
        int[][] dp = new int[n][m];
        dp[0][0] = grid[0][0];

        for (int i = 1; i < n; i++) {dp[i][0] = grid[i][0] + dp[i-1][0];}
        for (int j = 1; j < m; j++) {dp[0][j] = grid[0][j] + dp[0][j-1];}

        for (int i = 1; i < n; i++) {
            for (int j = 1; j < m; j++) {
                dp[i][j] = grid[i][j] + Math.min(dp[i-1][j], dp[i][j-1]);
            }
        }
        return dp[n-1][m-1];
    }
}
