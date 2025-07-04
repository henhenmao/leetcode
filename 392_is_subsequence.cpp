


/*
392. Is Subsequence (https://leetcode.com/problems/is-subsequence/description/?envType=study-plan-v2&envId=top-interview-150)
Follow up: Suppose there are lots of incoming s, say s1, s2, ..., sk where k >= 109, and you want to check one by one to see if t has its subsequence. In this scenario, how would you change your code?

have two pointers at the beginning of strings s and t
let p1 be the pointer for string s and p2 be the pointer for string t
increment p2 in the loop, if t[p2] == s[p1], we can increment p1 by one to check for the next letter

if p1 makes it to the end of string s, that means that all characters of s exist in t in the proper order
    we know that s is a subsequence of t

runtime: O(n) where n is the length of t
space: O(1)
*/

#include <iostream>
using namespace std;

bool isSubsequence(string s, string t) {

    if (s.length() > t.length()) {
        return false;
    }

    if (s == "") {
        return true;
    }

    int p2 = 0;
    int p1 = 0;

    while (p2 < t.length()) {
        if (s[p1] == t[p2]) {
            p1++;

            if (p1 == s.length()) {
                return true;
            }
        }
        p2++;
    }
    return false;
}


