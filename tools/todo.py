
import os
import re

"""
to-do list
run this to locate files that are marked NO, UF, or NC
too lazy to write it now i'll do it later    
"""

todos = ["UF", "NO", "NC", "AF"]

unfinished_files = []
non_optimal_files = []
no_comment_files = []
follow_up_files = []

divider = "----------------"

def display():

    def printFiles(files):
        for file, path in files:
            print(f"{file} at {path}")


    if unfinished_files:
        print(f"UNFINISHED FILES: {len(unfinished_files)}\n{divider}")
        printFiles(unfinished_files)
    else:
        print(f"no unfinished files :)")
    print()

    if unfinished_files:
        print(f"NON-OPTIMAL FILES: {len(non_optimal_files)}\n{divider}")
        printFiles(non_optimal_files)
    else:
        print(f"everything is optimal :)")
    print()

    if no_comment_files:
        print(f"NO COMMENTS FILES: {len(no_comment_files)}\n{divider}")
        printFiles(no_comment_files)
    else:
        print(f"everything is commented :)")
    print()

    if follow_up_files:
        print(f"FOLLOW UP FILES: {len(follow_up_files)}\n{divider}")
        printFiles(follow_up_files)
    else:
        print(f"no follow up questions :)")
    print()

        
def findUF():
    path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

    for dirpath, dirnames, filenames in os.walk(path):

        # skip the git directory (idk why it's there in the first place)
        if ".git" in dirnames:
            dirnames.remove(".git")
        if ".venv" in dirnames:
            dirnames.remove(".venv")
        if ".vscode" in dirnames:
            dirnames.remove(".vscode")
 
        # print(f"Directory: {dirpath}")
        for filename in filenames:
            res = [filename, os.path.join(dirpath, filename)]
            name, _ = os.path.splitext(filename) # separates file name and file extension
            if name.endswith("UF"):
                unfinished_files.append(res)
            elif name.endswith("NO"):
                non_optimal_files.append(res)
            elif name.endswith("NC"):
                no_comment_files.append(res)
            elif name.endswith("AF"):
                follow_up_files.append(res)

                
    display()

findUF()



    

    


