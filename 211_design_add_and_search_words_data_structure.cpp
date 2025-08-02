

/*
211. Design Add and Search Words Data Structure (https://leetcode.com/problems/design-add-and-search-words-data-structure/description/)

trie nodes
    create a trie node structure where each node has a hashmap children and boolean end
        children contains the letters that can possibly follow the current letter in a word added
            number of children for any node is at most 26 since there are only 26 letters
        end is true if the current node is the last letter in a word and false otherwise

contructor:
    create a single trie node with no children and is not the end of any word
    this will be the root of the prefix tree

addWord()
    each node represents a letter in a word
    starting at the root trie node of the prefix tree and iterating through each character in word
        keep track of the current trie node, let current node = curr, and the current character = c
        check if c exists in curr's children set, if yes, simply move to that new node
        if c does not exist as one of curr's children, simply create a new node where curr->children[c] = TrieNode()
    at the end of iterating over each character, the current node will end as the node representing the last letter of word
        because we are at the last letter, set curr->end = true

search()
    iterate over each character c in word to search 
    if c == '.', search through all of curr's children
    if c is anything else and c is not in curr's children, return false
    if the loop is over, curr is now at the last letter of the word, check if last letter is a last letter
        return true if curr->end == true and false otherwise

runtime:
    addWord: O(n) where n is the length of the word
    search() O(n) where n is the length of the world

space: O(t) where t is the number of nodes created
*/

#include <iostream>
#include <unordered_map>
#include <stack>
using namespace std;


struct TrieNode {
    unordered_map<char, TrieNode*> children;
    bool end = false;
    TrieNode() = default;
    ~TrieNode() {
        for (auto& pair : children) {
            delete pair.second;
        }
    }
};

class WordDictionary {
private:
    TrieNode* root;
public:
    WordDictionary() {
        root = new TrieNode();
    }
    
    void addWord(string word) {
        TrieNode* curr = root;
        for (char c : word) {
            if (curr->children.count(c) == 0) { // current character is not a child of current node
                curr->children[c] = new TrieNode();
            }
            curr = curr->children[c];
        }
        curr->end = true;
    }

    bool search(string& word, int i, TrieNode* curr) {
        if (i == word.length()) {
            return curr->end;
        }

        char c = word[i];

        // case 1: c is a wildcard
        if (c == '.') { // search all children
            for (const auto& pair : curr->children) {
                if (search(word, i+1, pair.second)) {
                    return true;
                }
            }
            return false;
        }

        // case 2: c is a letter
        if (curr->children.count(c) == 0) {
            return false;
        } else {
            return search(word, i+1, curr->children[c]);        
        }
        return curr->end;
    }
    
    bool search(string word) {
        TrieNode* curr = root;
        return search(word, 0, curr);
    }
};  

int main() {

    WordDictionary* wd = new WordDictionary();

    wd->addWord("a");
    wd->addWord("a");

    cout << wd->search("a") << endl;
    cout << wd->search(".") << endl;
    cout << wd->search("a.") << endl;

    return 0;
}