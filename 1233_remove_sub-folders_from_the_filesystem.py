
from typing import List

"""
1233. Remove Sub-Folders from the Filesystem (https://leetcode.com/problems/remove-sub-folders-from-the-filesystem/?envType=daily-question&envId=2025-07-19)

i just learned how to implement a trie prefix tree like yesterday and this question is looking awfully familiar....
this is a trie problem i'm like 99% sure

create a tree where each node is a folder name
for each filepath in the folder, split the file path by the '/' characters, this gives each folder in the path
    remove the last folder from the path and check if the remaining path exists in your folder tree
    if the path exists, current path is a subfolder of some other folder, do not add to the tree
    if the path does not exist, current path is not a subfolder of another folder, add the last folder to the tree

since we are going in order of each folder path in the input, we may encounter an input such as
    ["/a/b", "/a"], where the "/a/b" will be processed before the "/a" and "/a/b" will be added
    we can just sort the initial list of folder paths so that shorter file paths will always be ahead.

    
"""

class Folder:
    def __init__(self):
        self.children = {} 
        self.end = False # whether or not current folder is the end of a path

def removeSubfolders(folder: List[str]) -> List[str]:
    root = Folder()

    res_paths = []

    for path in folder:
        tokens = path.split("/")
        sub = False
        curr = root

        for token in tokens:
            if curr.end:
                sub = True
                break
            if token not in curr.children:
                curr.children[token] = Folder()
            curr = curr.children[token]
        
        if not sub:
            curr.end = True
            res_paths.append(path)
    
    return res_paths

print(removeSubfolders(["/a","/a/b","/c/d","/c/d/e","/c/f"]))

    
