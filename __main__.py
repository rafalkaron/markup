# coding: utf-8
"""
Batch-convert your docs.
"""

import os
import sys
import argparse
from MarkUP import (progressbar as pb,
                    convert_file,
                    convert_folder,
                    markdown_str_to_html_str,
                    html_str_to_markdown_str,
                    markdown_str_to_dita_str,
                    html_str_to_dita_str
                    )
__version__ = "0.3"
__author__ = "Rafał Karoń <rafalkaron@gmail.com>"

def main():
    par = argparse.ArgumentParser(description="Batch-convert Markdown and HTML files to DITA.", formatter_class=argparse.RawTextHelpFormatter)
    par.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    par.add_argument("input", type=str, help="provide a filepath to a file or a filder with files that you want to convert")
    par.add_argument("convert", type=str, help="""set the conversion type:
 * md_html - convert Markdown to HTML
 * md_dita - convert Markdown to DITA
 * html_md - Convert HTML to Markdown""")
    par.add_argument("-out", "--output", metavar="output_folder", help="manually specify the output folder (defaults to the input folder)")
    args = par.parse_args()

    sys.tracebacklimit = 0 # Disables traceback messages
    invalid_input = f" [!] {args.input} does not exist."

    # Set input and output folders
    if args.output:
        output_folder = args.output
    elif not args.output:
        output_folder = args.input

    # Convert MD to...
    if args.convert == "md_html":
        if os.path.isfile(args.input):
            convert_file(args.input, "md", markdown_str_to_html_str, "html")
        elif os.path.isdir(args.input):
            convert_folder(args.input, "md", markdown_str_to_html_str, output_folder, "html")
        else:
            raise Exception(invalid_input)
    elif args.convert == "md_dita":
        if os.path.isfile(args.input):
            convert_file(args.input, "md", markdown_str_to_dita_str, "dita")
        elif os.path.isdir(args.input):
            convert_folder(args.input, "md", markdown_str_to_dita_str, output_folder, "dita")
        else:
            raise Exception(invalid_input)

    # Convert HTML to...
    elif args.convert == "html_dita":
        if os.path.isfile(args.input):
            convert_file(args.input, "html", html_str_to_dita_str, "dita")
        elif os.path.isdir(args.input):
            convert_folder(args.input, "html", html_str_to_dita_str, output_folder, "dita")
        else:
            raise Exception(invalid_input)
    if args.convert == "html_md":
        if os.path.isfile(args.input):
            convert_file(args.input, "html", html_str_to_markdown_str, "md")
        elif os.path.isdir(args.input):
            convert_folder(args.input, "html", html_str_to_markdown_str, output_folder, "md")
        else:
            raise Exception(invalid_input)

if __name__ == "__main__":
    main()