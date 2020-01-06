__version__ = "0.1"
__author__ = "Rafał Karoń <rafalkaron@gmail.com.com>"

"""
    MarkUP Lite (Codename: Flamingo Parts)
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Convert all Markdown files in the MarkUP Lite directory to DITA.
    
    Uses: 
    - "mistune" to parse Markdown.
    - "markdown2dita" to convert Markdown to DITA.
"""

import mistune, os, glob

_markup_filepath = os.path.abspath(__file__)
_markup_filename = os.path.basename(__file__)
_markup_directory = _markup_filepath.replace(_markup_filename, "").replace("\\", "/")  

_markdown_files = glob.glob(_markup_directory + "/*.md")

for _markdown_file in _markdown_files:
    _md_to_dita = os.system("markdown2dita -i " + _markdown_file + " -o " + str(_markup_directory) + ".dita")

    
exit()