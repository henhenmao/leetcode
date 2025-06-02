
import os

"""
i will use this program to count the number of solutions in total
"""

def count():
    num_files = 0
    num_dirs = 0
    dir = os.getcwd()
    print(dir)

    for file in os.listdir(dir):
        if os.path.isdir(file):
            num_dirs += 1
            num_files += len(os.listdir(file))
        else:
            num_files += 1
    return f"there are probably {num_files} files and {num_dirs} directories in the current directory"

print(count())