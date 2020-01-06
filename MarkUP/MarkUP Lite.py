__version__ = "0.5"
__author__ = "Rafał Karoń <rafalkaron@gmail.com>"

"""
    MarkUP Lite (Codename: Well-fed Flamingo)
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Convert all Markdown files in the MarkUP Lite directory to DITA.
    
    Dependencies:
    Uses "markdown2dita" to convert Markdown to DITA. 
    "markdown2dita" uses "misuse" to parse Markdown.
"""

import mistune, os, glob, time, markdown2dita

_markup_filepath = os.path.abspath(__file__)
_markup_filename = os.path.basename(__file__)
_markup_directory = _markup_filepath.replace(_markup_filename, "").replace("\\", "/")  
_markdown_files = glob.glob(_markup_directory + "/*.md")
_markdown_files_uppercase = glob.glob(_markup_directory + "/*.MD")

print("Converting your Markdown files to DITA...")

for _markdown_file in _markdown_files:
    _md_to_dita = os.system("markdown2dita -i " + "\"" + _markdown_file + "\"" + " -o " + "\"" + _markdown_file.replace("md", "dita") + "\"")
for _markdown_file in _markdown_files_uppercase:
    _md_to_dita = os.system("markdown2dita -i " + "\"" + _markdown_file + "\"" + " -o " + "\"" + _markdown_file.replace("MD", "dita") + "\"")

print("Conversion successful!\nThis window will close automatically in 5 seconds.")
time.sleep(5)
exit()