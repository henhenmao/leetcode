


/*
1717. Maximum Score From Removing Substrings (https://leetcode.com/problems/maximum-score-from-removing-substrings/solutions/6992558/maximum-score-from-removing-substrings-beats-100/?envType=daily-question&envId=2025-07-23)

i couldn't solve this by myself so i'm following a leetcode solution

this is a greedy problem somehow i was convinced that this was a dynamic programming problem
    - always want to remove the substring with the higher value before the other
    - simulate the removal of substrings using stacks

algorithm:
    1. compare which of x and y is larger. let high = "ab" if x >= y and low = "ba" otherwise
    2. initialize am empty stack stack and traverse characters in s
        if the top of the stack + the current character = high, you have found a high value substring
        ex. 
            s = "abaa" where high = "ba"
            i = 0 -> stack.push("a")
            i = 1 -> check stack.top() + s[i] = "ab" != "ba" -> stack.push("b")
            i = 2 -> check stack.top() + s[i] = "ba" == "ba" -> add corresponding points for "ba" -> pop top of stack to remove the substring
        
        add max(x, y) to the total score count when the higher value substirng is found
        we do not push characters from the higher substring into the stack so it removes them
        
    3. after one pass of searching for high substring and getting scores, pop all elements from the stack into a new string remaining
        since doing this reverses the elements, reverse the string again to put elements back in order

    4. do the exact same thing with the remaining string and the stack but search for the lower value substring

runtime: O(n) where n is the length of s
space: O(n)
*/

#include <iostream>
#include <stack>
using namespace std;

int maximumGain(string s, int x, int y) {


    stack<char> stack;
    string higher = (x >= y) ? "ab" : "ba";
    string lower = (higher == "ab") ? "ba" : "ab";

    int higherScore = max(x, y);
    int lowerScore = min(x, y);
    int total = 0;


    // counting high priority substring
    for (char c : s) {
        if (!stack.empty() && (string("") + stack.top() + c == higher)) {
            stack.pop();
            total += higherScore;
        } else {
            stack.push(c);
        }
    }

    string remaining = "";
    while (!stack.empty()) {
        remaining += stack.top();
        stack.pop();
    }
    reverse(remaining.begin(), remaining.end());

    // counting low priority substring
    for (char c : remaining) {
        if (!stack.empty() && (string("") + stack.top() + c == lower)) {
            stack.pop();
            total += lowerScore;
        } else {
            stack.push(c);
        }
    }

    return total;
}

int main() {

    string s = "cdbcbbaaabab";
    int x = 4;
    int y = 5;

    cout << maximumGain(s, x, y) << endl;
    return 0;
}
