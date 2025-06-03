

import os

"""
i want to be able to search the name of a file and know if it exists and exactly where it is in the repository
"""


def search(file):

    path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

    matches = []

    for dirpath, dirnames, filenames in os.walk(path):

        if ".git" in dirnames:
            dirnames.remove(".git")
        
        for filename in filenames:
            if file in filename:
                matches.append(f"{filename} found in {dirpath}")

    if matches:
        print("possible matches\n───── ⋆⋅☆⋅⋆ ─────")
        for match in matches:
            print(match)
        print()
    else:
        print("no matches found....")
        print()


inp = input("what are you looking for: ")
search(inp)




