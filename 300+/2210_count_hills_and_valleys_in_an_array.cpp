

/*
2210. Count Hills and Valleys in an Array (https://leetcode.com/problems/count-hills-and-valleys-in-an-array/description/?envType=daily-question&envId=2025-07-27)

use a pointer to keep track of the index of the last distinct element of the last hill/valley
skip consecutive duplicates by skipping if nums[i] == nums[i+1]

this way we only look at the last element of each hill or valley to represent the entire area
    keeping track of the previous hill/valley's element to make comparisons


algorithm:
    1. iterate from index 1 to index nums.size()-1, skipping the leftmost and rightmost indices
    2. iitialize the element of the previous neighbor element at 0
    3. skip all elements where nums[i] == nums[i+1] to avoid duplicates
    4. when nums[i] != nums[i+1], check if nums[i] is a hill or valley
        nums[prev] = element of the previous neighbor
        nums[i+1] = element of the next neighbor
        check that nums[i] is less than both of them or greater than both of them
            add to count if true
    5. if nums[i] != nums[i+1], update previous to equal to i 
    
runtime: O(n) where n is the length of nums
space: O(1)
*/


#include <iostream>
#include <vector>
using namespace std;

int countHillValley(vector<int>& nums) {

    int count = 0;
    int prev = 0;
    for (int i = 1; i < nums.size()-1; i++) {
        if (nums[i] != nums[i+1]) { // not a conseucutive duplicate 
            if (nums[i] > nums[prev] && nums[i] > nums[i+1] || nums[i] < nums[prev] && nums[i] < nums[i+1]) { // is a hill or valley
                count++;
            }
            prev = i;
        }
    }
    return count;
}