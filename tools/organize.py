import os
import re # regex
import shutil

"""
- i used this to organize all questions into different folders
- intent was to organize questions into groups of 10 for easier access
- requires each question to be labelled with its question id at beginning of the file name
"""

def organize():
    dir = os.path.abspath(os.path.join(__file__, "..", ".."))
    print(dir)

    for file in os.listdir(dir):


        # skips everything that isn't a file or a git thing (mainly directories)
        if os.path.isdir(os.path.join(dir, file)) or ".git" in file:
            continue

        # uses regex to match the first found number in front of the file name
        # sets folder_name to the same number found in the file
        match = re.match(r'^(\d+)', file)
        if not match:
            continue

        # correlates the matched number to a folder interval
        n = int(match.group(1))
        start = (n // 10) * 10 + 1
        end = start + 9

        # i'm just gonna put all ids that are 500+ into one folder
        # might change the number if too many
        # i just don't want folders containing single files

        limit = 300
        if "_UF" in file:
            folder = f"unfinished"

        elif start >= limit:
            folder = f"{limit}+"
        else:
            folder = f"{int(start):03d}-{int(end):03d}" # pads the numbers to fit into three digits

        # checks if designated folder exists
        # if not then creates a new folder
        folder_path = os.path.join(dir, folder)
        if not os.path.exists(folder_path):
            os.mkdir(folder_path)

        # moves the file to the desginated folder
        src_path = os.path.join(dir, file)
        dst_path = os.path.join(folder_path, file)
        shutil.move(src_path, dst_path)
        print(f"Moved {file} to {folder}/")

organize()
        
        

        