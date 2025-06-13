

import os
import sys

"""
i want to be able to search the name of a file and know if it exists and exactly where it is in the repository
"""


def search(file):
    if file == "":
        print("empty input\n")
        return

    path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

    matches = []

    for dirpath, dirnames, filenames in os.walk(path):

        if ".git" in dirnames:
            dirnames.remove(".git")
        
        for filename in filenames:
            if file in filename:
                matches.append(f"{filename} at {os.path.join(dirpath, filename)}")

    if matches:
        print(f'possible matches for "{file}"\n────────── ⋆⋅☆⋅⋆ ──────────')
        for match in matches:
            print(match)
        print()
    else:
        print("no matches found....\n")

# take a command line argument if it exists
# if no command line argument, ask for an input
# if multiple command line arguments, return matches for each term

if len(sys.argv) < 2:
    inp = input("what are you looking for: ")
    print()
    search(inp)
    pass
else:
    print()
    for inp in sys.argv[1:]: # skip the search argument at index 0
        search(inp)




