

/*
169. Majority Element (https://leetcode.com/problems/majority-element/?envType=study-plan-v2&envId=top-interview-150)
Follow-up: Could you solve the problem in linear time and in O(1) space?

constant space algorithm: moores voting algorithm
    this algorithm takes advantage of the fact that there is an element that takes up at least half of the array's size

algorithm:  
    1. set curr = nums[0] and count = 1, count variable represents the number of votes that curr has 
    2. iterate through remaining elements of array
    3. if nums[i] == curr, increment count, represents a vote for the current leading party
    4. if nums[i] != curr, decrement count, represents a vote for an opposing party
    5. if count becomes 0 after a decrement, change curr to nums[i] and set count back to 1, represents another party taking the lead
    6. return curr at the end

due to the nature of the majority element taking up half of the array, it will always have the lead vote at the end of this

runtime: O(n) where n is the size of nums
space: O(1)
*/

#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;

int majorityElement(vector<int>& nums) {
    // can assume that a majority element always exists (no empty array)

    int curr = nums[0];
    int count = 1;

    for (int n : nums) {
        if (n == curr) {
            count++;
            continue;
        }
        count--;
        if (count == 0) {
            curr = n;
            count++; // sets count back to 1 for the new lead
        }
    }

    return curr;
}



/*
O(n) space algorithm:
    1.  create a frequency map of each distinct number in nums
    2. iterate through each freqeuncy
    3. if a frequency is greater than or equal to nums.size()//2

runtime: O(n) where n is the size of nums
space: O(n)

#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;

int majorityElement(vector<int>& nums) {
    unordered_map<int, int> freq;

    for (int n : nums) {
        freq[n]++;
    }

    for (auto& pair : freq) {
        if (pair.second > nums.size()/2) {
            return pair.first;
        }
    }
    return -1;
}
*/


