
/*
394. Decode String (https://leetcode.com/problems/decode-string/description/)

You may assume that the input string is always valid; there are no extra white spaces,
square brackets are well-formed, etc. Furthermore, you may assume that the original
data does not contain any digits and that digits are only for those repeat numbers, k.
For example, there will not be input like 3a or 2[4].

encoded string can have nested codes for example:
    s = "3[a2[c]]"
      = 3 * ("a" + 2 * "c")
      = 3 * ("acc")
      = "accaccacc"

we should decode the string recursively

iterate through the string until you come across an integer with an opening bracket after it
    keep in mind that the integer can be in the range [1, 300] so watch out for multiple digits
    find the index of the closing bracket

    recurse this into the string inside of the brackets
    continue the iteration at the index after the closing bracket

BRO I THINK YOU NEED TO USE A STACK WTF???
    WHEN FINDING THE INDEX OF THE RIGHT CLOSING BRACKET YOU CAN'T JUST USE THE FIRST CLOSING BRACKET YOU SEE
    SINCE YOU MIGHT COME ACROSS CLOSING BRACKETS THAT MATCH WITH OTHER BRACKETS
    YOU NEED TO USE A STACK TO MAKE SURE THAT THE BRACKETS YOU ARE LOOKING AT ARE RIGHT

when you find an operning bracket:
    create a stack containing literally anything just make sure it contains something
    as you are iterating and looking for the matching closing bracket:
        if you come across another opening bracket, add something to the stack
        if the come across a closing bracket, pop from the stack
            if you pop from the stack and the stack becomes empty, you are at the right matching closing bracket
brooooo

algorithm: 
    let an encoded message hold the form of n[s], where n is the multiplier and s is the string that gets multiplied
    1. create two strings nstr and decoded
    2. iterate through the current string s in a while loop, let c = the current character
        if c is a number: add the number to nstr
        if c is a letter: add the letter to decoded (just a regular letter with no multiplier)
    3. if c is an opening bracket, find the index of the matching closing bracket in the string
        create a stack initialized to {1}, this represents the opening bracket you just came across
        iterate through the string, let k = the current character
            if k is another opening bracket, push 1 to the stack
            if k is a closing bracket, pop 1 from the stack
                if you ever pop from the stack, if the stack is empty after popping, you are at the matching bracket
    4. once you have the index for the matching closing bracket, recurse all previous steps into the substring between the opening bracket and the closing bracket
    5. take the returned value of the recursion and multiply it n times, where n = integer value of nstr

runtime: O(n * k) where n is the size of the string, and k is the average number of times a string is repeated (k[string])
space: O(n * k)
*/

#include <iostream>
#include <ctype.h>
#include <stack>
using namespace std;

string decodeString(string s) {

    string nstr = "";
    string decoded = "";

    int i = 0;

    while (i < s.length()) {
        char c = s[i];
        if (isdigit(c)) {
            nstr += c; 
        } else if (c == '[') {

            stack<int> stack; // creating a stack to check for the right closing bracket 
            stack.push(1);

            i++;
            int j = i; // index after the opening bracket

            while (!stack.empty()) { // getting index of the closing bracket
                if (s[i] == '[') {
                    stack.push(1);
                } else if (s[i] == ']') {
                    stack.pop();
                }
                i++;
            }   
            i--; // moves i back so you don't include the closing bracket in temp_decode
                // the i++ at the end of the while loop will make up for this

            int n = stoi(nstr);
            string temp_decode = decodeString(s.substr(j, i-j)); // recursively getting the decoded contents inside the brackets    
            for (int k = 0; k < n; k++) { // adding the decoded contents n times
                decoded += temp_decode;
            }

            nstr.clear(); // clear the string for the next n[s] 

        } else {
            decoded += c;
        }

        i++;
    }

    // cout << "returning " << decoded << endl;
    return decoded;
}

int main() {

    string s = "2[abc]3[cd]ef";
    cout << decodeString(s) << endl;

    return 0;
}