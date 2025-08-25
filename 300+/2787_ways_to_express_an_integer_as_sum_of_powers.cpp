

/*
2787. Ways to Express an Integer as Sum of Powers (https://leetcode.com/problems/ways-to-express-an-integer-as-sum-of-powers/description/?envType=daily-question&envId=2025-08-12)
Since the result can be very large, return it modulo 10^9 + 7.

try every number from 1 to n to add n^x to the current sum
    if the current sum exceeds n, stop and add one to the totla
normal backtracking algorithm to find all possible sums of n consisting of powers of x

have a 2d dp table where each state of dp[curr][i] = the number of sets of unique integers that sum to n with a starting sum of dp[curr][i]

algorithm:
    1. 

runtime: O(n^2)
space: O(n^2)
*/

#include <iostream>
#include <vector>
using namespace std;

int numberOfWays(int n, int x, int i, int curr, vector<vector<int>>& dp, int MOD) {
    if (curr > n) return 0;
    if (curr == n) return 1;

    if (dp[curr][i] != -1) return dp[curr][i];

    int total = 0;
    for (int j = i; j <= n; j++) {
        long long next = curr+pow(j, x);
        if (next > n) break;
        total = (total +  numberOfWays(n, x, j+1, next, dp, MOD)) % MOD;
    }

    return dp[curr][i] = total;
}

int numberOfWays(int n, int x) {
    int MOD = 1e9 + 7;
    vector<vector<int>> dp(n+1, vector<int>(n+1, -1));
    return numberOfWays(n, x, 1, 0, dp, MOD);
}

int main() {
    int n = 11;
    int x = 1;

    cout << numberOfWays(n, x) << endl;
    return 0;
}