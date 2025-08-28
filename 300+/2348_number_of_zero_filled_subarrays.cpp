


/*
2348. Number of Zero-Filled Subarrays (https://leetcode.com/problems/number-of-zero-filled-subarrays/description/?envType=daily-question&envId=2025-08-24)

with an array of size n, there are (n*(n+1))/2 distinct subarrays you can get from the array

ex. [0] -> (1*2)/2 -> 1 subarray 
    [0,0,0] -> (3*4)/2 -> 6 subarrays
    [0,0,0,0,0] -> (5*6)/2 -> 15 subarrays

find all consecutive subarrays of all 0s in nums and get the lengths

ex. nums = [1,3,0,0,2,0,0,4] contains two subarrays of [0,0]
    [0,0] + [0,0] -> (2*3)/2 + (2*3)/2 = 6

algorithm:
    1. loop through nums to find consecutive zeros
    2. if a zero is encountered, increment currSize
    3. if a non-zero number is encountered, add the current currSize subarrays to the total -> total += ((long long) currSize*(currSize+1))/2
        make sure to convert one operand to a long long since the values can become very large
    4. in the case of a consecutive sequence of zeros being at the end, the loop will not count it
        simply add any remaining currSize subarrays to the total at the end before returning

runtime: O(n) where n is the size of nums
space: O(1)
*/

#include <iostream>
#include <vector>
using namespace std;

long long zeroFilledSubarray(vector<int>& nums) {
    long long total = 0;
    int currSize = 0;

    for (int n : nums) {
        if (n == 0) {
            currSize++;
        } else {
            total += ((long long) currSize*(currSize+1))/2;
            currSize = 0;
        }
    }
    total += ((long long) currSize*(currSize+1))/2; // adding the last consecutive 0 sequence if it exists at the end
    return total;
}

int main() {

    vector<int> nums = {1,3,0,0,2,0,0,0};
    cout << zeroFilledSubarray(nums) << endl;

    return 0;
}