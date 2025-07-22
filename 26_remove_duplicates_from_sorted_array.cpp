

/*
26. Remove Duplicates From Sorted Array (https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/)
Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

this question can basically be simplified into
    "if we traverse the array, how many unique values will be encountered?"
note that we are only concerned with the first k elements of nums, where k is the number of unique elements in nums

we can set two pointers, one at the beginning of nums and another for iterating over the array
    let curr = 1 and i iterating from 1 to end of nums
    every time a new unique element is seen, set nums[curr] = nums[i] and increment curr to the next index
        ignore curr = 0 since the first element is always a new element
        since nums is sorted, we know an element is unique if nums[i-1] != nums[i]
    in the end, curr will be incremented to k

runtime: O(n) where n is the size of nums
space: O(1)
*/


#include <iostream>
#include <vector>
using namespace std;

int removeDuplicates(vector<int>& nums) {
    int curr = 0;
    
    for (int i = 1; i < nums.size(); i++) {
        if (nums[i-1] != nums[i]) { // unique element!!!
            nums[curr] = nums[i];
            curr++;
        }
    }
    
    return curr;
}