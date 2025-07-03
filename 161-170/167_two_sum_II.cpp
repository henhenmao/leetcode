

/*
167. Two Sum II - Input Array Is Sorted (https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/)
Your solution must use only constant extra space.

since nums is already sorted in non-decreasing order, we will use a binary search on top of a linear search
use a linear loop for all values of index1, and use binary search to find if target-nums[index1] exists

"The tests are generated such that there is exactly one solution. You may not use the same element twice."
    make sure index1 and index2 are not the same
    since there is exactly one solution, this implies that there are no duplicates concerning values that are a part of the solution

oh yeah make sure your answers are 1-indexed for some reason the question makes you do that

algorithm:
    1. do a linear search for values of index1
    2. for each value of index1, do a binary search and try to find index2 = target-nums[index1]
    3. if index2 can be found, return index1 and index2
    4. if index2 is not found, iterate the first loop for a new value of index1
    

runtime: O(n * log(n)) where n is the length of nums
space: O(1)
*/

#include <iostream>
#include <vector>
using namespace std;

vector<int> twoSum(vector<int>& nums, int target) {
    int n = nums.size();
    vector<int> res;

    int temp;
    int low;
    int high;
    int mid;

    for (int i = 0; i < n; i++) { // i = index1

        // do a binary search for target-nums[i]
        temp = target-nums[i];
        low = 0;
        high = n-1;
        
        while (low <= high) {
            mid = (low + high)/2;

            if (nums[mid] == temp) {
                int index1 = i+1;
                int index2 = mid+1;

                if (mid == i) {
                    index2++;
                }

                res.push_back(index1);
                res.push_back(index2);
                return res;
            }

            if (nums[mid] > temp) { // overshot the sum, go back
                high = mid-1;
            } else {
                low = mid+1;
            }
        }
    }
    return res;
}

int main() {
    vector<int> nums = {1,2,3,4,4,9,56,90};
    int target = 8;

    vector<int> res = twoSum(nums, target);
    for (int n : res) {
        cout << n << " ";
    }
    cout << endl;

    return 0;
}