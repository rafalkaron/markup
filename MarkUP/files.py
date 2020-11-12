# coding: utf-8
__author__ = "Rafał Karoń <rafalkaron@gmail.com>"

import glob
import os
import sys

def files_list(directory, files_extension):
    """Return a list of files with a given extension in a directory."""
    files_list_lowercase = glob.glob(f"{directory}/*.{files_extension.lower()}")
    files_list_uppercase = glob.glob(f"{directory}/*.{files_extension.upper()}")
    files_list = files_list_lowercase + files_list_uppercase
    return files_list

def enter_filepath():
    """Manually enter file path."""
    filepath = input("Manually enter file path").replace("\"", "").replace("\'","")  
    return filepath

def read_file(filepath):
    """Return a string with file contents."""
    with open(filepath, mode='rt', encoding='utf-8') as f:
        return f.read()

def save_str_as_file(str, filepath):
    """Save a string to a file and return the file path.
    
    Keyword arguments:
    str - the string that you want to save as in a file
    filepath - the path to the file that you want to save the string to
    """
    with open(filepath, "w", encoding="utf-8") as file:
        file.write(str)
    return filepath

def file_extension(filepath):
    """Return file extension from a file path."""
    file_extension = os.path.splitext(filepath)[1][1:]
    return file_extension

def boolean_prompt(prompt_str):
    """Exit program on any other response than 'y' or 'Y'"""
    prompt = input(prompt_str)
    if prompt == "y" or prompt == "Y":
        pass
    elif prompt != "y" or prompt != "Y":
        print(f" [i] Cancelled.")
        sys.exit(0)