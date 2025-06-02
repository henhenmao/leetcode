import os

"""
learning how to use the os module
"""

for dirpath, dirnames, filenames in os.walk(os.getcwd()):

    # skip the git directory
    if ".git" in dirnames:
        dirnames.remove(".git")

    # print(f"Directory: {dirpath}")

    for filename in filenames:
        print(f"  File: {filename}")
