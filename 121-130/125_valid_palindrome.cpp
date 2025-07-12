

/*
125. Valid Palindrome (https://leetcode.com/problems/valid-palindrome/description/?envType=study-plan-v2&envId=top-interview-150)

1. remove all non-alphanumeric characters
2. convert all uppercase to lowercase
3. use two pointers to check if it is a palindrome or not

i'm too lazy to do this in place so i'm jsut going to build a new string with O(n) space complexity

runtime: O(n) where n is the size of string s
space: O(n) building new string
*/

#include <iostream>
#include <ctype.h>
#include <algorithm>
using namespace std;

bool isPalindrome(string s) {
    string fs = "";

    for (char c : s) {
        if (isalnum(c)) {
            fs += c;
        }
    }

    cout << fs << endl;

    int l = 0;
    int r = fs.length()-1;
    while (l < r) {
        if (tolower(fs[l]) != tolower(fs[r])) {
            return false;
        }
        l++;
        r--;
    }
    return true;
}

int main() {

    cout << isPalindrome("racar") << endl;
    return 0;
}
