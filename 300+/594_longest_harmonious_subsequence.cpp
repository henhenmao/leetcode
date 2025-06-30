


/*
594. Longest Harmonious Subsequence (https://leetcode.com/problems/longest-harmonious-subsequence/description/?envType=daily-question&envId=2025-06-30)

note: a harmonious sequence has a difference of exactly 1 between the min and max values
    this means that any valid subsequence will only contain two distinct values, each only 1 apart
    since we are finding subsequences and not sublists, we can just count frequencies of each number 
        find pairs of distinct values that are only 1 apart and add their frequencies together for the length of a valid subsequence

    gonna try this in cpp since i'm studying it

algorithm:
    1. create hashmap freq of the frequency of each number in nums
    2. for each key n in freq, check if n+1 exists as a key in nums
    3. if n and n+1 both exist as keys, add the two frequencies: this is the length of a possible harmonious subsequence
    4. keey track of the current longest harmonious subsequence you have

runtime: O(n) where n is the length of nums
space: O(n)

*/

#include <iostream>
#include <vector>
#include <unordered_map>


using namespace std;

int findLHS(vector<int>& nums) {

    int res = 0;
    unordered_map<int, int> freq; // key=number in nums, value=frequency

    // building the hashmap
    for (int n : nums) {
        freq[n] += 1;
    }

    for (auto [n, count] : freq) {
        cout << n << " " << count << endl;
    }

    // iterates through an unordered_map
    for (auto& [n, count] : freq) { 
        // check if key n+1 exists

        // NOTE: don't check freq[n+1] as it will insert that key into the hashmap if n+1 doesn't exist due to operator[]
        if (freq.count(n+1)) {
            int curr = count + freq[n+1];
            res = max(res, curr);
        }

    }

    cout << endl;
    for (auto [n, count] : freq) {
    cout << n << " " << count << endl;
    }

    return res;
}

int main() {
    // vector<int> nums = {1,3,5,7,9,11,13};
    // cout << findLHS(nums) << endl;

    return 0;
}