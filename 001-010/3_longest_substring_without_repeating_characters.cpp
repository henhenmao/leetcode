

/*
3. Longest Substring Without Repeating Characters (https://leetcode.com/problems/longest-substring-without-repeating-characters/description/)

initialize a set and two pointers left and right both starting at index 0

expand the right pointer to include new elements in a sliding window
    add all visited elements into the set

if a duplicate is encountered while expanding right
    shrink the window by shifting left pointer until the duplicate is removed
    remove all elements that left pointer traverses from the set
        since we are not including them in the window anymore

keep track of the longest window you have ever held
    the size of the current window is (right-left+1)

runtime: O(n) where n is the length of s
space: O(n)
*/

#include <iostream>
#include <vector>
#include <unordered_set>
using namespace std;

int lengthOfLongestSubstring(string s) {
    unordered_set<char> visited;

    int res = 0;

    int n = s.length();
    int left = 0;
    int right = 0;

    while (right < n) {
        while (visited.count(s[right])) { // duplicate element at s[right]
            visited.erase(s[left]);
            left++;
        }
        visited.insert(s[right]);
    
        res = max(res, right-left+1);

        right++;
    }

    return res;
}

int main() {

    string s = "bbbbb";
    
    cout << lengthOfLongestSubstring(s) << endl;

    return 0;
}