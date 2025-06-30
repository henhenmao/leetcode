


/*
20. Valid Parentheses (https://leetcode.com/problems/valid-parentheses/)

learning how to use c++ so redoing this question
*/

#include <iostream>
#include <stack>
#include <unordered_map>
using namespace std;

bool isValid(string s) {
    
    stack<char> stack;
    unordered_map<char, char> paras = {{'(', ')'}, {'[', ']'}, {'{', '}'}};

    for (char p : s) {
        // if opening bracket: push to stack
        if (p == '(' || p == '[' || p == '{') {
            stack.push(p);
        } else { // if closing bracket: check if bracket push is valid
            if (stack.empty() || paras[stack.top()] != p) {
                return false;
            }
            stack.pop();
        }
    }
    return stack.size() == 0;
}

int main() {
    cout << isValid("()") << endl;
    return 0;
}