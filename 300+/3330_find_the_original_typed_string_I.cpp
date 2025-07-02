


/*
3330. Find the Original Typed String I (https://leetcode.com/problems/find-the-original-typed-string-i/description/?envType=daily-question&envId=2025-07-01)

note that the mistake has happened at most once, so it may not have happened at all

ex. "abbcccc"
    focusing on the substring "cccc", instead of this, alice may have meant to type: "ccc", "cc", or "c"
    focusing on the substring "bb", instead of this, alice may have meant to type "b"

we take each substring of consecutive equal characters and add its length-1 to the total
add 1 to the end of the total to represent the case of alice never have made a mistake

i honestly can't remember how to easily split a string into it's consecutive characteres

algorithm:
    1. have a pointer i at the start of the string
    2. keep track of the character c at the start of the stirng
    3. iterate i until you find a character not equal to c, keep track of the count
    4. when character not equal to c, count is the length of consecutive letter substring
    5. add count-1 to the result
    6. set new character c at the next substring
    7. repeat previous steps until i reaches the end
    8. add 1 to the result to represent the case where alice doesn't make a mistake

runtime: O(n) where n is the length of word
space: O(1)
*/

#include <iostream>
using namespace std;

int possibleStringCount(string word) {

    int res = 0;
    char c = word[0];
    int i = 0;
    int count;

    while (i < word.length()) {
        count = 0;

        while (word[i] == c) {
            count++;
            i++;
        }

        res += (count-1);
        c = word[i];
    }

    return res+1;
}

int main() {
    string word = "aaaa";
    cout << possibleStringCount(word) << endl;

    return 0;
}