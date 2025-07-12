


/*
179. Largest Number (https://leetcode.com/problems/largest-number/description/)

convert each number in nums to a string
sort the new array lexicographically in non-ascending order
put them together???
i'll see what happens surely there's more than that

ok turns out you can't just sort the string array in descending order
but you just need to make a small change
add a lambda comparator that takes in two strings a and b
    orders strings a and b based on which is larger: a+b or b+a
this fully ensures that the sorting results in the largest number from the string array

runtime: O(n * log(n) * k), where n is the size of nums and k is the average number of digits per element in nums
space: O(n * k)
*/

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

string largestNumber(vector<int>& nums) {
    vector<string> strnums;
    string res = "";
    for (int n : nums) {
        strnums.push_back(to_string(n));
    }

    // make sure adjacent elements form the largest numbers possible
    sort(strnums.begin(), strnums.end(), [](string& a, string& b) {
        return a + b > b + a;
    });

    for (string s : strnums) {
        res += s;
    }

    return (res[0] != '0') ? res : "0";
}

int main() {
    vector<int> nums = {3, 30, 34, 5, 9};
    cout << largestNumber(nums) << endl;
    return 0;
}