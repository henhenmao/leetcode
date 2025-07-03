

/*
162. Find Peak Element (https://leetcode.com/problems/find-peak-element/description/)
You must write an algorithm that runs in O(log n) time.

note that nums[i] != nums[i + 1] for all valid i. this means that there aren't any adjacent duplicates

when doing binary search and at a mid index, check the neighbors of the middle index
    if nums[mid+1] < nums[mid], we know that one of the values to the left of mid (or mid itself) is a peak
    if nums[mid+1] > nums[mid], we know that one of the values to the right of mid (not mid) is a peak
    nums[mid+1] != nums[mid] due to the constraints of the problem

return left point at the end


runtime: O(log(n))
space: O(1)
*/

#include <iostream>
#include <vector>
using namespace std;

int findPeakElement(vector<int>& nums) {
    
    int n = nums.size();
    int low = 0;
    int high = n-1;

    while (low < high) {
        int mid = (low + high)/2;

        if (nums[mid+1] < nums[mid]) {
            high = mid;
        } else {
            low = mid+1;
        }        
    }
    return low;
}