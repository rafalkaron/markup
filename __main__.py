# coding: utf-8
"""
Batch-convert Markdown and HTML files.
"""

import os
import sys
import argparse
from MarkUP import (md_dita,
                    md_html,
                    html_md,
                    html_dita)
__version__ = "0.5"
__author__ = "Rafał Karoń <rafalkaron@gmail.com>"
def main():
    #sys.tracebacklimit = 0 # Disable traceback messages
    par = argparse.ArgumentParser(description="Batch-convert Markdown and HTML files.", formatter_class=argparse.RawTextHelpFormatter)
    par.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    par.add_argument("input", type=str, help="provide a filepath to a file or a folder with files that you want to convert")
    par.add_argument("convert", type=str, help="""set the conversion type:
 * md_dita - convert Markdown to DITA
 * html_dita - convert HTML to DITA
 * md_html - convert Markdown to HTML
 * html_md - convert HTML to Markdown""")
    par.add_argument("-out", "--output", metavar="output_dir", help="manually specify the output folder (defaults to the input folder)")
    args = par.parse_args()

    # Input and output folders
    if args.output:
        output_dir = args.output
    elif not args.output:
        if os.path.isfile:
            output_dir = os.path.dirname(args.input)
        elif os.path.isdir:
            output_dir = args.input

    # Make paths uniform for every platform
    args.input = args.input.replace("\\", "/")
    output_dir = output_dir.replace("\\", "/")

    # Conversion types
    if args.convert == "md_html":
        md_html(args.input, output_dir)
    elif args.convert == "md_dita":
        md_dita(args.input, output_dir)
    elif args.convert == "html_dita":
        html_dita(args.input, output_dir)
    elif args.convert == "html_md":
        html_md(args.input, output_dir)
    else:
        print(" [!] Run MarkUP again and set an allowed conversion type.\n")
        par.print_help()

if __name__ == "__main__":
    main()