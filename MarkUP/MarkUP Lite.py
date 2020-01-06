__version__ = "0.2"
__author__ = "Rafał Karoń <rafalkaron@gmail.com.com>"

"""
    MarkUP Lite (Codename: Modest Flamingo)
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Convert all Markdown files in the MarkUP Lite directory to DITA.
    
    Dependencies:
    Uses "markdown2dita" to convert Markdown to DITA. 
    "markdown2dita" uses "mustune" to parse Markdown.

    Upcoming features:
    - Support for uppercase extensions.
"""

import mistune, os, glob, time

_markup_filepath = os.path.abspath(__file__)
_markup_filename = os.path.basename(__file__)
_markup_directory = _markup_filepath.replace(_markup_filename, "").replace("\\", "/")  
_markdown_files = glob.glob(_markup_directory + "/*.md")

print("Converting your Markdown files to DITA...")

for _markdown_file in _markdown_files:
    _md_to_dita = os.system("markdown2dita -i " + "\"" + _markdown_file + "\"" + " -o " + "\"" + _markdown_file.replace("md", "dita") + "\"")

print("Conversion successful!\nThis window will close automatically in 5 seconds.")
time.sleep(5)
exit()