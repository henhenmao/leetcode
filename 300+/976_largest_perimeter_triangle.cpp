
/*
976. Largest Perimeter Triangle (https://leetcode.com/problems/largest-perimeter-triangle/?envType=daily-question&envId=2025-09-28)

the hard part about this problem is realizing that the triangle with most perimeter will also be three consecutive elements in a sorted array

we can use a sorting + sliding window greedy approach to solve this problem
    1. sort the array in descending order
        better to start with the larger values
    2. iterate with a sliding window of size 3 until nums.size()-2
    3. check if nums[i], nums[i+1], or nums[i+2] can form a valid triangle
        you can just check the condition of nums[i+2]+nums[i+1] > nums[i] to see if triangle is valid
    4. since the array in descending order, the moment you find a valid triangle, simply return the sum of nums[i], nums[i+1], and nums[i+2]

runtime: O(n logn)
space: O(1)
*/


#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int largestPerimeter(vector<int>& nums) {
    sort(nums.begin(), nums.end(), greater<int>());

    int n = nums.size();
    for (int i = 0; i < n-2; i++) {
        if (nums[i+2] + nums[i+1] > nums[i]) {
            return nums[i+2] + nums[i+1] + nums[i];
        }
    }
    return 0;
}

int main() {
    return 0;
}