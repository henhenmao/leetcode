



/*
966. Vowel Spellchecker (https://leetcode.com/problems/vowel-spellchecker/solutions/7187439/super-simple-easy-clean-vowel-error-spellchecker/?envType=daily-question&envId=2025-09-14)

three cases for each query

1. query matches to a word exactly with no mistakes (case sensitive)
2. query matches to a word to capitalization (case-insensitive)
3. query matches to a word to vowel errors

create three different data structures 
1. create a set containing all words in wordList
2. create a hash map mapping all lowercase version of each word to the actual word
    only need to map the first match in the wordList
3. create a hash map mapping each word with their vowels removed to the actual word
    replace each vowel with a wildcard like '#' to maintain proper ordering of characters
    only need to map the first match in the wordList

for each query, check each data structure 1 by 1 in the proper order
add to the result the first match found from exact match -> capital match -> vowel match

runtime: O(n + m) where n is the size of wordlist and m is the size of queries
space: O(n)
*/


#include <iostream>
#include <vector>
#include <unordered_map>
#include <unordered_set>
#include <cctype>
using namespace std;

// returns lowercase of inputted string without modifying the origiinal string
string toLowercase(string s) {
    transform(s.begin(), s.end(), s.begin(), [](unsigned char c) {return tolower(c);});
    return s;
}

string removeVowels(string& s) {
    string vowels = "AEIOUaeiou";
    string res;
    for (char c : s) {
        if (vowels.find(c) == std::string::npos) {
            res += c;
        } else {
            res += '#';
        }
    }
    return res;
}

vector<string> spellchecker(vector<string>& wordlist, vector<string>& queries) {
    vector<string> res;
    unordered_set<string> matches;
    unordered_map<string, string> capitalMatches;
    unordered_map<string, string> vowelMatches;

    for (string word : wordlist) {
        matches.insert(word);
        string capitalMatch = toLowercase(word);
        string vowelMatch = removeVowels(capitalMatch);
        
        if (capitalMatches.count(capitalMatch) == 0) {
            capitalMatches[capitalMatch] = word;
        }

        if (vowelMatches.count(vowelMatch) == 0) {
            vowelMatches[vowelMatch] = word;
        }
    }

    for (string query : queries) {
        if (matches.count(query) != 0) {
            res.push_back(query);
            continue;
        }

        string capitalMatch = toLowercase(query);
        if (capitalMatches.count(capitalMatch) != 0) {
            res.push_back(capitalMatches[capitalMatch]);
            continue;
        }

        string vowelMatch = removeVowels(capitalMatch);
        if (vowelMatches.count(vowelMatch) != 0) {
            res.push_back(vowelMatches[vowelMatch]);
            continue;
        }

        res.push_back("");
    }

    return res;
}


int main() {

    vector<string> wordlist = {"KiTe","kite","hare","Hare"};
    vector<string> queries = {"kite","Kite","KiTe","Hare","HARE","Hear","hear","keti","keet","keto"};

    string s = "keet";
    string v = toLowercase(s);
    string b = removeVowels(v);
    cout << b << endl;


    vector<string> res = spellchecker(wordlist, queries);
    for (string s : res) {
        cout << s << " ";
    }
    cout << endl;

    return 0;
}