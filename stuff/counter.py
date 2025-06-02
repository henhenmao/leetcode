
import os

"""
i will use this program to count the number of solutions in total
i actually have no idea how accurate this is
"""

def count():
    num_files = -1 # readme.md gets counted
    num_dirs = 0

    print(os.getcwd())
    print(os.path.dirname(os.getcwd()))
    
    for dirpath, dirnames, filenames in os.walk(os.path.dirname(os.getcwd())):

        if ".git" in dirnames:
            dirnames.remove(".git")
            
        if "stuff" in dirnames:
            dirnames.remove("stuff")

        for filename in filenames:
            print(filename)
            num_files += 1
        
        num_dirs += len(dirnames)
    
    return f"there are probably {num_files} files and {num_dirs} directories in the current directory"

print(count())