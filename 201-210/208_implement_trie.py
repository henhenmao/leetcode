


"""
208. Implement Trie (Prefix Tree) (https://leetcode.com/problems/implement-trie-prefix-tree/?envType=study-plan-v2&envId=top-interview-150)

insert() inserts word into the trie
search(word) returns true if word exists in the trie, false otherwise
startsWith(prefix) returns true if there is a previously inserted word in the trie that begins with prefix, false otherwise

insert and search functions can be easily implemented with a hash map
main problem is the implementation of the startsWith() function 
    searching each word in the trie for the prefix slow

insert(word):
    we need to create a prefix tree as our trie
        each node in the tree will represent a character for a word
        ex. insert("hello")
            root -> 'h' -> 'e' -> 'l' -> 'l' -> 'o'
            mark the 'o' node with something to indicate that it is the end of a word
        
            insert("hella")
            since "hello" and "hella" share the same first four characters we can now reuse the existing tree
                simply add another node after the last 'l' node containing an 'a'
                the last 'l' node now has two children: 'o' and 'a'
                also mark 'a' as the end of a word
        
search(word):
    given a prefix tree and a word to search for, we can just follow the tree with each character in word
    if a character doesn't exist in the tree, return false
    if you find a path of characters in the prefix tree that equals to word, check that the last character is marked as the last character
        if not marked, return false
        if marked, return true

startsWith(word):
    follow the tree for each character in word
    if path doesn't exist, return false
    else return true

runtime:
    insert(word): O(n) where n is the length of word
    search(word): O(n) where n is the length of word 
    startsWith(prefix): O(n) where n is the length of the prefix

space: O(t) where t is the total number of nodes created in the prefix tree
"""

class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False 

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root

        # finding/creating a path from word[0] to word[-1] in the prefix tree
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]

        curr.end = True # marking last letter of inserted word as the last letter


    def search(self, word: str) -> bool:
        curr = self.root

        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        
        return curr.end # returns false is last letter is not the last letter to any word
        

    def startsWith(self, prefix: str) -> bool:
        curr = self.root

        # simply follow path and return false if you cannot proceed further
        for c in prefix:
            if c not in curr.children:
                return False
            curr = curr.children[c]

        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)