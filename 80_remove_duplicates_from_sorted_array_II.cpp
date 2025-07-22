

/*
80. Remove Duplicates From Sorted Array II (https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/description/?envType=study-plan-v2&envId=top-interview-150)
Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

i feel like i can just do the exact same thing as 26. Remove Duplicates From Sorted Array I but just keep track of the current number
    keep track of whether or not you have or have not seen two or more of the current number
        if you have already seen 2 of nums[i], and there is another nums[i], skip it

algorithm:
    1. set curr to index 1 since the first element is ignored as it will always be included in the result array
    2. set count = 1 to represent count of times we have seen the current element (first element)
    3. loop from i = 1 to end of nums
        if nums[i-1] == nums[i], you have a duplicate element, increment count by 1
        if nums[i-1] != nums[i], we have found a new unique element, reset count back to 1
    4. only set nums[curr] = nums[i] if count of current element is less than or equal to 2
        we ignore all elements of nums[i] if nums[i] has already been seen twice in the past

runtime: O(n) where n is the length of nums
space: O(1)

*/

#include <iostream>
#include <vector>
using namespace std;

int removeDuplicates(vector<int>& nums) {
    if (nums.size() <= 2) {
        return nums.size();
    }

    int curr = 1;
    int count = 1;

    for (int i = 1; i < nums.size(); i++) {

        if (nums[i-1] == nums[i]) {
            count++;
        } else {
            count = 1;
        }

        // only make changes to nums if the count of the current element is 2 or less
        if (count <= 2) {
            nums[curr] = nums[i];
            curr++;
        }
    }
    return curr;
}

int main() {
    vector<int> nums = {1,1,1,2,2,3};
    int res = removeDuplicates(nums);

    for (int n : nums) {
        cout << n << " ";
    }
    cout << endl;
    cout << res << endl;


    return 0;
}