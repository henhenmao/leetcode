


/*
611. Valid Triangle Number (https://leetcode.com/problems/valid-triangle-number/?envType=daily-question&envId=2025-09-26)

valid traingle = given sides a, b, and c, the sum of any two sides must be greater than the third side
    in this case we can just check for a 

similar to 3sum solution

1. sort nums
2. for each value of nums[i], set left and right pointers at 0 and nums.size()-1
3. shift the left and right pointers 




*/

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int triangleNumber(vector<int>& nums) {
    sort(nums.begin(), nums.end());
    int n = nums.size();
    int count = 0;

    for (int i = n - 1; i >= 2; i--) {
        int left = 0;
        int right = i - 1;
        while (left < right) {
            if (nums[left] + nums[right] > nums[i]) {
                count += right - left;
                right--;
            } else {
                left++;
            }
        }
    }
    return count;
}

int main() {
    vector<int> nums = {2, 2, 3, 4};
    cout << triangleNumber(nums) << endl;
    return 0;
}