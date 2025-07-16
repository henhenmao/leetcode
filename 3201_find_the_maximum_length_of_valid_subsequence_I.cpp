

/*
3201. Find the Maximum Length of Valid Subsequence I (https://leetcode.com/problems/find-the-maximum-length-of-valid-subsequence-i/description/?envType=daily-question&envId=2025-07-16)

for each subsequence from nums:
    we need to check that each instance of (sub[i] + sub[i+1]) % 2 is the same

start each sequence at length two with sub = nums[i] + nums[i+1]
    record whether or not (nums[i] + nums[i+1]) % 2 is a 1 or 2
    let int parity = (nums[i] + nums[i+1]) % 2

for each subsequence of length two you make, just do a standard backtracking recursion to find all different subsequences
    you can either add nums[i] to your subsequence or not add nums[i] to your subsequence
    you cannot add nums[i] to your subsequence if (nums[i] + sub[sub.size()-1]) % 2 != parity

since we need the parity to be the same across all pairs in the subsequence, there are three possibilities for the largest valid subsequence
    1. all evens
    2. all odds
    3. strictly alternating between even and odd (which can then be divided into two more sub possibilities)
        a. strictly alternating between even and odd, starting with an odd integer
        b. strictly alternating between even and odd, starting with an even integer

    can just count the even and odd frequencies and mainly compute the largest length of an alternating subsequence

getting max alternating subsequence:
    start two separate recursive calls on the first even number and the first odd number in nums
        if there are no even numbers, you can conclude that the largest valid subsequence is every even number and vice versa
    
    keep track of the even odd state of the previous number added to subsequence (sub[sub.size()-1])
    for each value of nums[i], if nums[i]%2 != previous state, it is alternating and you can add nums[i] to the subsequence
        don't actually need to keep track of the subsequence, can just add 1 to be accumulated over the recursion

THIS SOLUTION IS TERRIBLE I THINK
IT'S LATE AT NIGHT AND I WAS DESPERATE TO FINISH THIS PROBLEM :(
I MEAN IT WORKS 

runtime: O(n) where n is the size of nums
space: O(n)
*/

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

// prev = previous state of even or odd, true = odd, false = even
int alternatingSubsequence(vector<int>& nums, int i, bool prev, vector<vector<int>>& dp) {
    if (i == nums.size()) {
        return 0;
    }

    if (dp[i][prev] != -1) {
        return dp[i][prev];
    }

    // choose to not include nums[i] into sub
    int no = alternatingSubsequence(nums, i+1, prev, dp);

    int yes = 0;
    if (nums[i] % 2 != prev) {
        yes = 1 + alternatingSubsequence(nums, i+1, nums[i]%2, dp);
    }

    dp[i][prev] = max(yes, no);
    return dp[i][prev];
}

int maximumLength(vector<int>& nums) {

    // counting odds ands evens
    int odds = 0, evens = 0;
    for (int n : nums) {
        if (n % 2 == 0) {
            evens++;
        } else {
            odds++;
        }
    }

    if (odds == 0 || evens == 0) {
        return max(odds, evens);
    }

    // computing the largest alternating subsequence
    int oddAlternating = 0;
    int evenAlternating = 0;

    vector<int> evensub;
    vector<int> oddsub;

    vector<vector<int>> even_dp(nums.size()+1, vector<int>(2, -1));
    vector<vector<int>> odd_dp(nums.size()+1, vector<int>(2, -1));

    for (int i = 0; i < nums.size(); i++) {
        if (nums[i] % 2 == 0) {
            evenAlternating = alternatingSubsequence(nums, i, true, even_dp);
            break;
        }
    }

    for (int i = 0; i < nums.size(); i++) {
        if (nums[i] % 2 == 1) {
            oddAlternating = alternatingSubsequence(nums, i, false, odd_dp);
            break;
        }
    }

    // cout << "odd alternating: " << oddAlternating << endl;
    // cout << "even alternating: " << evenAlternating << endl;

    return max(max(evenAlternating, oddAlternating), max(odds, evens));
}

int main() {

    vector<int> nums = {1,2,3,4};
    cout << maximumLength(nums) << endl;

    return 0;
}