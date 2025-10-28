

/*
2221. Find Triangular Sum of an Array (https://leetcode.com/problems/find-triangular-sum-of-an-array/description/?envType=daily-question&envId=2025-09-30)

we just need to find the ones digit of the triangular sum of the starting list

example 1: nums = [1,2,3]
[1,2,3]
 [3,5]
  [8]

row 2 = [[1+2], [2+3]]
row3 = [[1+2]+[2,3]]

the [1] is counted 1 time
the [2] is counted 2 times
the [3] is counted 1 time

example 2: nums = [1,2,3,4]
[1,2,3,4]
 [3,5,7]
  [8,12]
   [20]

row 2 = [[1+2], [2+3], [3+4]]
row 3 = [[1+2]+[2+3], [2+3]+[3+4]]
row 4 = [[1+2]+[2+3]+[2+3]+[3+4]]

the [1] is counted 1 times
the [2] is counted 3 times
the [3] is acounted 3 times
the [4] is counted 1 times

example 3: nums = [1,2,3,4,5]
[1,2,3,4,5]
 [3,5,7,9]
  [8,12,16]
    [20,28]
     [48]

row 2 = [[1+2], [2+3], [3+4], [4+5]]
row 3 = [[1+2]+[2+3], [2+3]+[3+4], [3+4]+[4+5]]
row 4 = [[1+2]+[2+3]+[2+3]+[3+4], [2+3]+[3+4]+[3+4]+[4+5]]
row 5 = [[1+2]+[2+3]+[2+3]+[3+4]+[2+3]+[3+4]+[3+4]+[4+5]]

the [1] is counted 1 times
the [2] is counted 4 times
the [3] is counted 6 times
the [4] is counted 4 times
the [5] is counted 1 times

im lowkey not good enough to solve this with combinatorics im just going to simulate it with a slower runtime

for n-1 rows, since the process is repeated by "removing" an element from nums until the size is 1
    iterate from j to n-i-1, which is the number of elements in the current row minus 1
        at each index j, we replace nums[j] with (nums[j] + nums[j+1]) % 10
            this effectively simulates the process of adding adjacent values together
at the end of this process, the ones digit of the triangular sum should be at the first index of nums

runtime: O(n^2) where n is the length of nums
space: O(1)
*/

#include <iostream>
#include <vector>
using namespace std;

int triangularSum(vector<int>& nums) {
    int n = nums.size();
    for (int i = 0; i < n-1; i++) {
        for (int j = 0; j < n-i-1; j++) {
            nums[j] = (nums[j+1] + nums[j]) % 10;
        }
    }
    return nums[0];
}

int main() {
    vector<int> nums = {1,2,3,4,5};
    cout << triangularSum(nums) << endl;
}
