

/*
509. Fibbonaci Number (https://leetcode.com/problems/fibonacci-number/)

this queston can easily be solved for small inputs with recursion

let fib(n) represent fib(n)

for fib(n), return fib(n-1) + fib(n-2)
    since fib(0) = 0 and fib(1) = 1, we use this as our base case and return n if (n <= 1)

fibbonaci repeats a lot of computataions
ex. fib(5) returns fib(4) + fib(3)
    fib(4) returns fib(3) + fib(2)
    fib(3) returns fib(2) + fib(1)
    
    notice how there are multiple calls to fib(3) and fib(2)
    if the inital value of n is a large number, there will be many many repeated calls that increase exponentially

    we can memoize computed fibbonaci numbers in a vector
    for example, the first time we call fib(3), we find fib(2) and fib(1) as usual
    once we have the returned value for fib(3), we put that value in some vector
    after that, every time we need to access the value of fib(3), instead of calculating it all again with fib(2) and fib(1)
        we can just access the vector for the value

algorithm: 
    1. create a memoization table of size n+1 filled with -1
    2. base case: return n if (n <= 1)
    3. if current fib(n) has been calculated already (not a -1), just return that value
    4. if current fib(n) has not been calculated (is a -1), compute the value with fib(n-1) + fib(n-2)
        and memoize the value in the table 

runtime: O(n) since each value of fib(n) is only computed once
space: O(n)
*/


#include <iostream>
#include <vector>
using namespace std;

int betterFib(int n, vector<int>& dp) {
    if (n <= 1) {
        return n;
    }

    if (dp[n] != -1) {
        return dp[n];
    }

    dp[n] = betterFib(n-1, dp) + betterFib(n-2, dp);
    return dp[n];
}

int fib(int n) {
    vector<int> dp((n+1), -1);
    return betterFib(n, dp);
}