
/*
290. Word Pattern (https://leetcode.com/problems/word-pattern/?envType=study-plan-v2&envId=top-interview-150)

all words in s are separated by a single space

find a way to split string s into separate words using " " as a delimiter

afterwards, iterate through pattern and words in s and charToWord corresponding letters in pattern to each word using a hash map
if a pair of pattern and word already exists, check that they are the same
    if they are not the same, the pattern does not charToWord and you can return false

no two letters map to the same word, and no two words map to the same letter
    because of this, we need two separate hash maps, one with letter to word pair, and one with word to letter pair
    letter to word hash map checks that no two letters map to the same word
    word to letter hash map checks that no two words map to the same letter

if you make it to the end, everything matches and you can return true

runtime: O(n) where n is the length of string s
space: O(n)
*/


#include <iostream>
#include <vector>
#include <sstream>
#include <unordered_map>

using namespace std;


bool wordPattern(string pattern, string s) {

    // splits the string by spaces
    // puts each word into vector words
    istringstream iss(s);
    vector<string> words;
    string word;
    while (iss >> word) {
        words.push_back(word);
    }

    if (pattern.length() != words.size()) {
        return false;
    }

    unordered_map<char, string> charToWord;
    unordered_map<string, char> wordToChar;

    for (int i = 0; i < pattern.length(); i++) {
        char currChar = pattern[i];
        string currWord = words[i];

        // check that no two letters map to the same word 
        // no two words charToWord to the same letter

        if (wordToChar.count(currWord) > 0 && currChar != wordToChar[currWord] ||
        charToWord.count(currChar) > 0 && currWord != charToWord[currChar]) {
            return false;
        } else {
            wordToChar[currWord] = currChar;
            charToWord[currChar] = currWord;
        }
    }
    return true;
}

int main() {

    string pattern = "abba";
    string s = "dog cat cat dog";
    cout << wordPattern(pattern, s) << endl;
    return 0;
} 