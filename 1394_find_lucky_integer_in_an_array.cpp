


/*
1394. Find Lucky Integer in an Array (https://leetcode.com/problems/find-lucky-integer-in-an-array/?envType=daily-question&envId=2025-07-05)

this is just a standard hash map problem
use a hash map to count frequencies of each distinct integer in array

iterate through each key value pair in the frequency map
    if the key is equal to its frequency, it is a lucky integer
    keep track of the largest lucky integer as you iterate

runtime: O(n)
space: O(n)
*/

#include <iostream>
#include <unordered_map>
#include <vector>
using namespace std;

int findLucky(vector<int>& arr) {
    unordered_map<int, int> freq;
    for (int n : arr) {
        freq[n]++;
    }

    int res = -1;
    for (const auto& pair : freq) {
        if (pair.first == pair.second) {
            res = max(res, pair.first);
        }
    }
    return res;
}