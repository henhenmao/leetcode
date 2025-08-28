

/*
386. Lexicographical Numbers (https://leetcode.com/problems/lexicographical-numbers/description/?envType=daily-question&envId=2025-08-24)

use a trie to get all numbers in lexicographical order
imagine a prefix tree where each node represents a digit for a number
    since 1 <= n <= 5 * 10^4, we only need to go down at most 4 levels deep 

if we do a preorder dfs traversal on this prefix tree, we will get the lexicographical sorted order of all numbers

at every recursive call, keep track of the current number = curr
    when travelling to a deeper node, multiply curr by 10 and add the new node to curr
    if the current number becomes greater than n (the largest number in the range), backtrack 
    add all numbers below or equal to n to the result vector

runtime: O(n)
space: O(1)

*/


#include <iostream>
#include <vector>
using namespace std;

void dfs(int n, int curr, vector<int>& res) {
    if (curr > n) return;

    res.push_back(curr);

    for (int i = 0; i <= 9; i++) {
        dfs(n, curr*10+i, res);
    }
}

vector<int> lexicalOrder(int n) {
    vector<int> res;
    for (int i = 1; i <= 9; i++) {
        dfs(n, i, res);
    }
    return res;
}

int main() {
    int n = 13;
    vector<int> res = lexicalOrder(n);

    for (int n : res) {
        cout << n << " ";
    }
    cout << endl;

    return 0;
}