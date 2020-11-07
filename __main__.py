# coding: utf-8
"""
Batch-convert your docs.
"""

import os
import sys
import re
import argparse
import time
from MarkUP import (progressbar as pb,
                    exit_prompt,
                    markdown_str_to_html_str,
                    html_str_to_markdown_str,
                    markdown_str_to_dita_str,
                    html_str_to_dita_str,
                    read_file,
                    enter_filepath,
                    save_str_as_file,
                    files_list,
                    file_extension,
                    convert_file,
                    convert_folder
                    )
__version__ = "0.3"
__author__ = "Rafał Karoń <rafalkaron@gmail.com>"

def exe_dir():
    """Return the executable directory."""
    if getattr(sys, 'frozen', False):
        exe_path = os.path.dirname(sys.executable)
        exe_path = os.path.dirname(os.path.dirname(os.path.dirname(exe_path))) # Uncomment for macOS app builds
    elif __file__:
        exe_path = os.path.dirname(__file__)
    return exe_path

def main():
    sys.tracebacklimit = 0 # Disables traceback messages
    par = argparse.ArgumentParser(description="Batch-convert Markdown and HTML files to DITA.", formatter_class=argparse.RawTextHelpFormatter)
    par.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    par.add_argument("-in", "--input", metavar="source", help="manually specify the input folder (defualts to MarkUP executable folder)")
    par.add_argument("-out", "--output", metavar="output_folder", help="manually specify the output folder (defaults to the input folder)")
    par.add_argument("-md_html", "--markdown_to_html", action="store_true", help="convert Markdown files to HTML files")
    par.add_argument("-html_md", "--html_to_markdown", action="store_true", help="convert HTML files to Markdown files")
    par.add_argument("-md_dita", "--markdown_to_dita", action="store_true", help="convert Markdown files to DITA files")
    par.add_argument("-html_dita", "--html_to_dita", action="store_true", help="convert HTML files to DITA files")
    par.add_argument("-ex", "--exit", action ="store_true", help="exits without a prompt (defaults to prompt on exit)")
    args = par.parse_args()

    # Default behavior. Sets source and output folders to the executable directory.
    if not args.input:
        source = exe_dir()
    elif args.input:
        source = args.input
    if not args.output:
        output_folder = source
    elif args.output:
        output_folder = args.output

    # Convert MD to...
    if args.markdown_to_html:
        if os.path.isfile(source):
            convert_file(source, "md", markdown_str_to_html_str, "html")
        elif os.path.isdir(source):
            convert_folder(source, "md", markdown_str_to_html_str, output_folder, "html")
        else:
            raise Exception("The resource that you selected does not exist.")
    elif args.markdown_to_dita:
        if os.path.isfile(source):
            convert_file(source, "md", markdown_str_to_dita_str, "dita")
        elif os.path.isdir(source):
            convert_folder(source, "md", markdown_str_to_dita_str, output_folder, "dita")
        else:
            raise Exception("The resource that you selected does not exist.")

    # Convert HTML to...
    elif args.html_to_dita:
        if os.path.isfile(source):
            convert_file(source, "html", html_str_to_dita_str, "dita")
        elif os.path.isdir(source):
            convert_folder(source, "html", html_str_to_dita_str, output_folder, "dita")
        else:
            raise Exception("The resource that you selected does not exist.")
    if args.html_to_markdown:
        if os.path.isfile(source):
            convert_file(source, "html", html_str_to_markdown_str, "md")
        elif os.path.isdir(source):
            convert_folder(source, "html", html_str_to_markdown_str, output_folder, "md")
        else:
            raise Exception("The resource that you selected does not exist.")
    
    # If no argumets are passed, display help.
    elif not args.markdown_to_html and not args.html_to_markdown and not args.markdown_to_dita and not args.html_to_dita and not args.exit:
        par.print_help()
    
    # Display Exit prompt if not overriden by an attribute
    if not args.exit:
        exit_prompt("To exit MarkUP, press [Enter]")

if __name__ == "__main__":
    main()