

/*
2044. Count Number of Maximum Bitwise-OR Subsets (https://leetcode.com/problems/count-number-of-maximum-bitwise-or-subsets/description/?envType=daily-question&envId=2025-07-28)

do a recursive backtracking algorithm to compute the bitwise or of all subsets
just do a standard O(2^n) subsets recursive backtracking, while keeping track of the bitwise OR of each current subset
keep track of the current maximum value bitwise OR and the total count of the maximum bitwise OR value

runtime: O(2^n) where n is the size of nums
space: O(n)
*/

#include <iostream>
#include <vector>
using namespace std;

void countMaxOrSubsets(vector<int>& nums, int curr, int& currMax, int& total, int i) {
    if (i == nums.size()) {

        if (curr > currMax) {
            currMax = curr;
            total = 1;
        } else if (curr == currMax) {
            total++;
        }

        return;
    }

    countMaxOrSubsets(nums, curr, currMax, total, i+1);
    countMaxOrSubsets(nums, curr|nums[i], currMax, total, i+1);
}

int countMaxOrSubsets(vector<int>& nums) {
    int currMax = 0;
    int total;
    countMaxOrSubsets(nums, 0, currMax, total, 0);
    return total;
}

int main() {
    vector<int> nums = {2,2,2};
    cout << countMaxOrSubsets(nums) << endl;
    return 0;
}

