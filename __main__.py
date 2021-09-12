# coding: utf-8
"""
Batch-convert Markdown and HTML files.
"""

import argparse
from MarkUP import (Source)

__version__ = "0.6.3"
__author__ = "Rafał Karoń <rafalkaron@gmail.com>"


def main():
    # sys.tracebacklimit = 0 # Disable traceback messages
    par = argparse.ArgumentParser(
        description="Batch-convert Markdown and HTML files.", formatter_class=argparse.RawTextHelpFormatter)
    par.add_argument("-v", "--version", action="version",
                     version=f"%(prog)s {__version__}")
    par.add_argument(
        "input", type=str, help="provide a filepath to a file or a folder with files that you want to convert")
    par.add_argument("convert", type=str, help="""set the conversion type:
    * md_dita - convert Markdown to DITA
    * html_dita - convert HTML to DITA
    * md_html - convert Markdown to HTML
    * html_md - convert HTML to Markdown""")
    par.add_argument("-out", "--output", metavar="folder_path", default="",
                     help="manually specify the output folder (defaults to the input DITA file folder)")
    args = par.parse_args()

    source = Source(args.input, args.convert, args.output)
    Source.output_files = source.convert()


if __name__ == "__main__":
    main()
