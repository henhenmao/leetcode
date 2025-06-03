
import os

"""
i will use this program to count the number of solutions in total
i actually have no idea how accurate this is
"""

def count():
    num_files = -1 # readme.md gets counted
    num_dirs = 0

    # print(os.getcwd()) gets the current working directory, not the directory the script is located in

    path = os.path.abspath(os.path.join(__file__, "..", ".."))
    print(f"searching {path}")
    
    for dirpath, dirnames, filenames in os.walk(path):

        if ".git" in dirnames:
            dirnames.remove(".git")
            
        if "stuff" in dirnames:
            dirnames.remove("stuff")

        
        num_files += len(filenames)
        num_dirs += len(dirnames)
    
    return f"there are probably {num_files} files and {num_dirs} directories in the current directory"

print(count())