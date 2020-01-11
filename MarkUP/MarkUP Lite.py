__version__ = "0.6"
__author__ = "Rafał Karoń <rafalkaron@gmail.com>"

"""
    MarkUP Lite (Codename: Functioning Flamingo)
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Convert all Markdown files in the MarkUP Lite directory to DITA.
    
    Dependencies:
    Uses "markdown2dita" to convert Markdown to DITA. 
    "markdown2dita" uses "misuse" to parse Markdown.
"""

import os, glob, time, re

#Global Variables
_markup_filepath = os.path.abspath(__file__)
_markup_filename = os.path.basename(__file__)
_markup_directory = _markup_filepath.replace(_markup_filename, "").replace("\\", "/")
_markdown_files = glob.glob(_markup_directory + "/*.md")
_markdown_files_uppercase = glob.glob(_markup_directory + "/*.MD")
_markdown_files_all = list(set(_markdown_files + _markdown_files_uppercase))

def intro():
    print("Converting your Markdown files to DITA...")

def convert():
    for _markdown_file in _markdown_files_all:
        os.system("markdown2dita -i " + "\"" + _markdown_file + "\"" + " -o " + "\"" + re.sub("md", "dita", _markdown_file, flags=re.IGNORECASE) + "\"")

def summary():
    print("Conversion successful!\nThis window will close automatically in 5 seconds.")
    time.sleep(5)

intro()
convert()
exit()