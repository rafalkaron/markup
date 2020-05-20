# coding: utf-8
__author__ = "Rafał Karoń <rafalkaron@gmail.com>"

import os
import sys
import glob

def exe_dir():
    """Return the executable directory."""
    if getattr(sys, 'frozen', False):
        exe_path = os.path.dirname(sys.executable)
    elif __file__:
        exe_path = os.path.dirname(__file__)
    return exe_path

def dir_files(directory, files_extension):
    """Return a list of files with a given extension in a directory"""
    files_extension_lowercase = str(files_extension).lower
    files_extension_uppercase = str(files_extension).upper
    files_list_lowercase = glob.glob(directory + f"/*.{files_extension_lowercase}")
    files_list_uppercase = glob.glob(directory + f"/*.{files_extension_uppercase}")
    files_list = list(set(files_list_lowercase + files_list_uppercase))
    return files_list

def enter_filepath():
    """Enter the \"My Clippings.txt\" file path.
    This function is called as a fallback of the "get_clipps_filepath()" function."""
    clipps_path = input("""
Klipps cannot locate the \"My Clippings.txt\" file that is usually in the \"documents\" directory on your Kindle.
    
Before running Klipps again, ensure that:
  * You highlighted some quotes while reading on your Kindle
  * Your Kindle is connected to and discovered by your computer
    NOTE: Some third-party USB cables may prevent your computer from correctly discovering your Kindle.

You can manually enter the \"My Clippings.txt\" file path or press [Enter] to exit Klipps: """).replace("\"", "").replace("\'","")
    filepath_exist = os.path.isfile(clipps_path)
    if filepath_exist == False:
        sys.exit(0)    
    return clipps_path

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