

/*
1295. Find Numbers with Even Number of Digits (https://leetcode.com/problems/find-numbers-with-even-number-of-digits/?envType=daily-question&envId=2025-09-16)

create a function that takes in a number n and returns the number of digits in the number
    repeatedly divide n by 10 until the number becomes 0, counting the number of times you divided by 10

for each number in nums, increment the total if the number has an even number of digits

runtime: O(n) where n is the length of nums
space: O(1)
*/

#include <iostream>
#include <vector>
using namespace std;

int numDigits(int n) {
    if (n == 0) return 0;
    return 1 + numDigits(n/10);
}

int findNumbers(vector<int>& nums) {
    int res = 0;
    for (int n : nums) {
        if (numDigits(n) % 2 == 0) res++;
    }
    return res;
}

