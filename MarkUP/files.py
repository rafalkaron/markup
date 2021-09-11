# coding: utf-8
__author__ = "Rafał Karoń <rafalkaron@gmail.com>"

import glob


def files_list(directory, files_extension):
    """Return a list of files with a given extension in a directory."""
    files_list_lowercase = glob.glob(
        f"{directory}/*.{files_extension.lower()}")
    files_list_uppercase = glob.glob(
        f"{directory}/*.{files_extension.upper()}")
    files_list = files_list_lowercase + files_list_uppercase
    return files_list


def read_file(filepath):
    """Return a string with file contents."""
    with open(filepath, mode='rt', encoding='utf-8') as f:
        return f.read()


def save_str_as_file(str, filepath) -> str:
    """Save a string to a file and return the file path.

    Keyword arguments:
    str - the string that you want to save as in a file
    filepath - the path to the file that you want to save the string to
    """
    with open(filepath, "w", encoding="utf-8") as file:
        file.write(str)
    return filepath
