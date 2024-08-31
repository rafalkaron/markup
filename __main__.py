# coding: utf-8
"""
Batch-convert Markdown and HTML files.
"""

import argparse

from MarkUP import Source

__version__ = "0.7.3"
__author__ = "Rafał Karoń <rafalkaron@gmail.com>"


def main():
    # sys.tracebacklimit = 0 # Disable traceback messages
    par = argparse.ArgumentParser(
        description="Batch-convert Markdown and HTML files.",
        formatter_class=argparse.RawTextHelpFormatter,
    )
    par.add_argument(
        "-v", "--version", action="version", version=f"%(prog)s {__version__}"
    )
    par.add_argument(
        "input",
        type=str,
        help="a path to a file or a directory that contains files to convert.",
    )
    par.add_argument(
        "conversion_type",
        type=str,
        help="""one of the following:
    * md_dita - converts Markdown to DITA.
    * html_dita - converts HTML to DITA.
    * md_html - converts Markdown to HTML.
    * html_md - converts HTML to Markdown.""",
    )
    par.add_argument(
        "-out",
        "--output",
        metavar="folder_path",
        default="",
        help="(optional) directory for the converted files (defaults to the input directory).",
    )
    args = par.parse_args()

    source = Source(args.input, args.conversion_type, args.output)
    Source.output_files = source.convert()


if __name__ == "__main__":
    main()
