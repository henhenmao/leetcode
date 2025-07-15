

/*
3136. Valid Word (https://leetcode.com/problems/valid-word/description/?envType=daily-question&envId=2025-07-15)

A word is considered valid if:
    It contains a minimum of 3 characters.
    It contains only digits (0-9), and English letters (uppercase and lowercase).
    It includes at least one vowel.
    It includes at least one consonant.

iterate through each character of the word and tick off each condition
check that all conditions are fulfilled at the end of the iteration

use a set or even a vector containing vowels and consonants (will be constant time lookup either way)

runtime: O(n) where n is the length of the word
space: O(1)
*/

#include <iostream>
#include <unordered_set>
#include <cctype>
using namespace std;

bool isValid(string word) {
    if (word.length() < 3) {
        return false;
    }

    unordered_set<char> vowels{'a', 'e', 'i', 'o', 'u'};
    bool vowelExists = false;
    bool consonantExists = false;

    for (char c : word) {
        if (!isalnum(c)) {
            return false;
        }

        if (isalpha(c)) {
            if (vowels.find(tolower(c)) == vowels.end()) { // is a consonant
                consonantExists = true;
            } else {
                vowelExists = true;
            }
        }
    }

    return consonantExists && vowelExists;
}

int main() {

    string word = "AhI";
    cout << isValid(word) << endl;


    return 0;
}