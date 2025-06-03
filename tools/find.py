
import os
import re

"""
run this to locate files that are marked NO, UF, or NC
too lazy to write it now i'll do it later    
"""

unfinished_files = []
non_optimal_files = []
no_comment_files = []
divider = "----------------"

def display():

    print()

    if unfinished_files:
        print(f"UNFINISHED FILES: {len(unfinished_files)}\n{divider}")
        for file in unfinished_files:
            print(file)
    else:
        print(f"no unfinished files :)")

    print()

    if unfinished_files:
        print(f"NON-OPTIMAL FILES: {len(non_optimal_files)}\n{divider}")
        for file in non_optimal_files:
            print(file)
    else:
        print(f"everything is optimal :)")

    print()

    if no_comment_files:
        print(f"NO COMMENTS FILES: {len(no_comment_files)}\n{divider}")
        for file in no_comment_files:
            print(file)
    else:
        print(f"everything is commented :)")
    print()

        
def findUF():
    path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

    for dirpath, dirnames, filenames in os.walk(path):

        # skip the git directory (idk why it's there in the first place)
        if ".git" in dirnames:
            dirnames.remove(".git")

        # print(f"Directory: {dirpath}")
        for filename in filenames:
            name, _ = os.path.splitext(filename) # separates file name and file extension
            if name.endswith("UF"):
                unfinished_files.append(filename)
            elif name.endswith("NO"):
                non_optimal_files.append(filename)
            elif name.endswith("NC"):
                no_comment_files.append(filename)
    display()




findUF()



    

    


