


/*
279. Perfect Squares (https://leetcode.com/problems/perfect-squares/description/)

perfects squares is literally the same thing as 322. Coin Change problem i'm pretty sure
the only difference is that your coins always are the set of perfect square numbers

algorithm:
    1. compute your "coins" by calculate every perfect square number less than or equal to n
        add all perfect squares into a vector and reverse the order (since largest should be checked first)
    2. call a dfs function to check combinations of perfect squares while keeping track of the sum
        backtrack when needed to avoid redundant paths
    3. use a dp table to reuse paths

runtime: O(n * n^0.5) at most n^0.5 perfect squares for an input of n, looped over n times in the recursive dfs
space: O(n) dp array
*/

#include <iostream>
#include <vector>

using namespace std;


void dfs(vector<int>& squares, vector<int>& dp, int& res, int i, int total, int count, int n) {
    if (i == squares.size() || total > n || count >= res) {
        return;
    }
    if (total == n) {
        res = min(res, count);
        return;
    }
    if (dp[total] <= count) {
        return;
    }

    dp[total] = count;

    for (int j = i; j < squares.size(); j++) {
        dfs(squares, dp, res, j, total+squares[j], count+1, n);
    }
}

int numSquares(int n) {
    vector<int> squares;
    int res = n+1;
    vector<int> dp(10001, n+1);
    
    int i = 1;
    while (i*i <= n) {
        squares.push_back(i*i);
        i++;
    }

    reverse(squares.begin(), squares.end());
    dfs(squares, dp, res, 0, 0, 0, n);
    return res;
}


// int main() {
//     cout << numSquares(101) << endl;
//     return 0;
// }