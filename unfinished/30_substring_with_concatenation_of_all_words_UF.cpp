



/*
30. Substring with Concatenation of All Words (https://leetcode.com/problems/substring-with-concatenation-of-all-words/description/)

current idea:
    create a frequency hashmap with each word in words as a key
        each value for the key of a word is the number of times it appears in words
        ex. words = ["hello", "henry", "hello", "abcde"]
            freq = {"hello":2, "henry":1, "abcde":1}    
    
    since all words in words are the same length, we know that a concatenation permutation in s will be of size
        words.size() * k, where k is the length of each string in words
    
    get all substrings of size words.size() * k, check if it is a valid concatenation
        check if all words exist

this solution is too slow -> TLES on last few cases
*/

#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;

    bool checkSubstring(unordered_map<string, int> freq, string s, int k) {

        for (int i = 0; i < s.size(); i+=k) {
            string word = s.substr(i, k);
            if (freq.count(word) == 0 || freq[word] == 0) {
                return false;
            }
            freq[word]--;
        }
        // cout << "return true!!!" << endl;
        return true;
    }

    vector<int> findSubstring(string s, vector<string>& words) {

        vector<int> res;

        int n = words.size();
        int k = words[0].length();
        int concatSize = n * k;

        if (concatSize > s.size()) {
            return res;
        }

        unordered_map<string, int> freq;
        for (string word: words) {
            freq[word]++;
        }

        int i = 0;
        while (i <= s.length()-concatSize) {
            // cout << "checking " << s.substr(i, concatSize) << endl;
            if (checkSubstring(freq, s.substr(i, concatSize), k)) {
                res.push_back(i);
            }
            i++;
        }
        return res;
    }

int main() {
    
    string s = "barfoothefoobarman";
    vector<string> words = {"foo","bar"};
    vector<int> res = findSubstring(s, words);
    for (int i : res) {
        cout << i << " ";
    }
    cout << endl;

    return 0;
}
