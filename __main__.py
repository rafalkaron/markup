# coding: utf-8
"""
Batch-convert Markdown and HTML files to DITA.
"""

import os
import sys
import re
import argparse
from MarkUP import (progressbar,
                    exit_prompt,
                    markdown_str_to_html_str,
                    read_file,
                    enter_filepath,
                    save_str_as_file,
                    files_list)

__version__ = "0.1"
__author__ = "Rafał Karoń <rafalkaron@gmail.com>"

def main():
    par = argparse.ArgumentParser(description="Batch-convert Markdown and HTML files to DITA.", formatter_class=argparse.RawTextHelpFormatter)
    par.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    par.add_argument("-in", "--input", metavar="input_folder", help="manually specify the input folder (defualts to MarkUP executable folder)")
    par.add_argument("-out", "--output", metavar="output_folder", help="manually specify the output folder (defaults to the input folder)")
    par.add_argument("-ex", "--exit", action ="store_true", help="exits without a prompt (defaults to prompt on exit)")
    args = par.parse_args()

    if getattr(sys, 'frozen', False):
        exe_path = os.path.dirname(sys.executable)
    elif __file__:
        exe_path = os.path.dirname(__file__)

    if not args.input:
        input_folder = exe_path
    if args.input:
        input_folder = args.input
    print(f"Converting the files from {input_folder}:")

    if not args.output:
        output_folder = input_folder
    if args.output:
        output_folder = args.output
    
    for input_file in files_list(input_folder, "md"):
        print(input_file)
        input_file_str = read_file(input_file)
        markdown_str = markdown_str_to_html_str(input_file_str)
        output_file = os.path.basename(re.sub(r".md", ".html", input_file, flags=re.IGNORECASE))
        print(output_file)
        save_str_as_file(markdown_str, output_folder + "/" + output_file)

    if not args.exit:
        exit_prompt("\nTo exit MarkUP, press [Enter]")

if __name__ == "__main__":
    main()