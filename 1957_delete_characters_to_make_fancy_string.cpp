

/*
1957. Delete Characters to Make Fancy String (https://leetcode.com/problems/delete-characters-to-make-fancy-string/description/?envType=daily-question&envId=2025-07-21)

algorithm:
    1. set the current character to s[0] and set a current count to 1, initialize result string with s[0]
    2. iterate through the string from 1 to s.length()-1
    3. if s[i] is equal to current character, increment the current count
            only add s[i] to result string if the current count is less than 3
        if s[i] is not equal to the current character
            reset current character to s[i]
            reset current count to 1
            add s[i] to the result, since the current count is 1 and less than 3

runtime: O(n) where n is the size of s
space: O(n)
*/


#include <iostream>
#include <vector>
using namespace std;

string makeFancyString(string s) {

    char curr = s[0];
    int currCount = 1;
    string res = "";
    res += curr;
    
    for (int i = 1; i < s.length(); i++) {
        if (s[i] == curr) {

            currCount++;
            if (currCount < 3) {
                res += s[i];
            }

        } else {

            curr = s[i];
            currCount = 1;
            res += s[i];

        }
    }

    return res;
}

int main() {

    string s = "aaabaaaa";
    cout << makeFancyString(s) << endl;

    return 0;
}