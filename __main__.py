# coding: utf-8
"""
Batch-convert your docs.
"""

import os
import sys
import argparse
from MarkUP import (progressbar as pb,
                    md_dita,
                    md_html,
                    html_md,
                    html_dita)
__version__ = "0.3"
__author__ = "Rafał Karoń <rafalkaron@gmail.com>"

def main():
    par = argparse.ArgumentParser(description="Batch-convert Markdown and HTML files to DITA.", formatter_class=argparse.RawTextHelpFormatter)
    par.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    par.add_argument("input", type=str, help="provide a filepath to a file or a filder with files that you want to convert")
    par.add_argument("convert", type=str, help="""set the conversion type:
 * md_html - convert Markdown to HTML
 * md_dita - convert Markdown to DITA
 * html_md - convert HTML to Markdown
 * html_dita - convert HTML to DITA""")
    par.add_argument("-out", "--output", metavar="output_dir", help="manually specify the output folder (defaults to the input folder)")
    args = par.parse_args()

    sys.tracebacklimit = 0 # Disables traceback messages

    # Set input and output folders
    if args.output:
        output_dir = args.output
    elif not args.output:
        output_dir = args.input

    if args.convert == "md_html":
        md_html(args.input, output_dir)
    elif args.convert == "md_dita":
        md_dita(args.input, output_dir)
    elif args.convert == "html_dita":
        html_dita(args.input, output_dir)
    elif args.convert == "html_md":
        html_md(args.input, output_dir)

if __name__ == "__main__":
    main()