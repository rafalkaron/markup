# coding: utf-8
"""
Batch-convert Markdown and HTML files to DITA.
"""

import argparse
from MarkUP import (progressbar,
                    exit_prompt,
                    markdown_str_to_html_str,
                    exe_dir,
                    read_file,
                    enter_filepath,
                    save_str_as_file,
                    dir_files)

__version__ = "0.1"
__author__ = "Rafał Karoń <rafalkaron@gmail.com>"

def main():
    par = argparse.ArgumentParser(description="Batch-convert Markdown and HTML files to DITA.", formatter_class=argparse.RawTextHelpFormatter)
    par.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    par.add_argument("-in", "--input", metavar="input_folder", help="manually specify the input folder (defualts to MarkUP executable folder)")
    par.add_argument("-out", "--output", metavar="output_folder", help="manually specify the output folder")
    par.add_argument("-ex", "--exit", action ="store_true", help="exits without a prompt (defaults to prompt on exit)")
    args = par.parse_args()

    if not args.input:
        in_path = exe_dir
    if args.input:
        in_path = args.input
    if not args.output:
        out_path = f"{os.path.normpath(os.path.expanduser('~/Desktop'))}/{os.path.basename(in_path)}".replace(".txt", ".html").replace("\\", "/").replace("//", "/")
    if args.output:
        out_path = f"{args.output}/{os.path.basename(in_path)}".replace(".txt", ".html").replace("\\", "/").replace("//", "/")
    
    if not args.exit:
        exit_prompt("\nTo exit Klipps, press [Enter]")

if __name__ == "__main__":
    main()