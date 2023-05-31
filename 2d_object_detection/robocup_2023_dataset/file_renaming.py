"""
This script is used to rename files in a directory.

Inputs:
- Parent directory path
- File extension
- New file name initial
- New file name starting index

Features:
- Keep the original files
- New renamed files will be stored in a new destination folder
- Print the old and new file names
- Print the total number of files renamed

"""

import os
import sys
import shutil

# GLOBAL INPUTS - CHANGE THESE ACCORDINGLY
PARENT_DIR = "<path to parent directory>"

FILE_EXTENSION = ".jpg"

NEW_FILE_NAME_INITIAL = "<new file name initial>" # script will add starting index to this
NEW_FILE_NAME_STARTING_INDEX = 0 # starting index

# *******************
# NOTE: destination folder name will be parent folder name + starting index + ending index
# *******************


def renaming_files():
    """
    This function is used to rename files in a directory.

    """
    FILE_COUNT = 0

    # get the total number of files in the directory
    TOTAL_NUMBER_OF_FILES = len([name for name in os.listdir(PARENT_DIR) if os.path.isfile(os.path.join(PARENT_DIR, name))])

    # add starting index and ending index in the destination folder name
    # example: Destination folder name: destination_folder_00000_00010
    global NEW_FILE_NAME_STARTING_INDEX
    DESTINATION_DIR = PARENT_DIR + "_" + str(NEW_FILE_NAME_STARTING_INDEX).zfill(5) + "_" + str(NEW_FILE_NAME_STARTING_INDEX + TOTAL_NUMBER_OF_FILES - 1).zfill(5)

    # check if destination folder exists, if not create it
    if not os.path.exists(DESTINATION_DIR):
        os.makedirs(DESTINATION_DIR)

    # sort the files in the directory
    for file_name in sorted(os.listdir(PARENT_DIR)):
        if file_name.endswith(FILE_EXTENSION):
            # take starting index in 5 digits 00000
            new_file_name = NEW_FILE_NAME_INITIAL + str(NEW_FILE_NAME_STARTING_INDEX).zfill(5) + FILE_EXTENSION

            # print the old and new file names
            print("Renaming file: ", file_name, "   ----->  ", new_file_name)
            
            # Use shutil.copy() instead of os.rename() to keep the original file
            shutil.copy(os.path.join(PARENT_DIR, file_name), os.path.join(DESTINATION_DIR, new_file_name))

            # increment count
            NEW_FILE_NAME_STARTING_INDEX += 1
            FILE_COUNT += 1
            

    # statistics
    print("Total number of files renamed: ", FILE_COUNT)

def check_folder_exists():
    """
    This function is used to check if the folder exists.

    """
    if not os.path.exists(PARENT_DIR):
        print("Folder does not exist")
        sys.exit()

    # check if the folder is empty
    if not os.listdir(PARENT_DIR):
        print("Folder is empty")
        sys.exit()

# Driver Code
if __name__ == '__main__':
    check_folder_exists()
    renaming_files()

    print("Done renaming files")
