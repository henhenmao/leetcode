

/*
1695. Maximum Erasure Value (https://leetcode.com/problems/maximum-erasure-value/description/?envType=daily-question&envId=2025-07-22)

this question is very similar to 3. Longest Substring Without Repeating Characters 
    where i used a sliding window with two pointers and a visited set
    so i'm just going to do the exact same thing 

algorithm:
    1. set two pointers left and right at index 0, initialize a set to keep track of visited elements
    2. shift the right pointer and add all encountered elements into visited
        also add all elements to a current sum, while keeping track of the largest sum you have seen so far
    3. if nums[right] already exists in visited, we shift the left pointer until nums[right] does not exist in visited anymore
        this makes sure we never can have a duplicate value in the window
        also make sure to subtract all removed elements from the current sum
    
runtime: O(n) where n is the size of nums
space: O(n)
*/

#include <iostream>
#include <vector>
#include <unordered_set>
using namespace std;

int maximumUniqueSubarray(vector<int>& nums) {
    
    unordered_set<int> visited;

    int n = nums.size();
    int left = 0, right = 0;
    int currSum = 0, maxSum = 0;

    while (right < n) {
        while (visited.count(nums[right])) {
            visited.erase(nums[left]);
            currSum -= nums[left];
            left++;
        }

        currSum += nums[right];
        maxSum = max(maxSum, currSum);
        visited.insert(nums[right]);
        right++;
    }

    return maxSum;
}

int main() {

    vector<int> nums = {5,2,1,2,5,2,1,2,5};
    cout << maximumUniqueSubarray(nums) << endl;
    return 0;
}