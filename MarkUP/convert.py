# coding: utf-8
__author__ = "Rafał Karoń <rafalkaron@gmail.com>"

import mistune
import markdown2dita
import tomd
import re
import random
import string
import time
import os
from .files import read_file, save_str_as_file, files_list, file_extension
from .feedback import progressbar as pb



def markdown_str_to_html_str(markdown_str, output_file):
    "Return an HTML string from a Markdown string."
    converter = mistune.markdown # or markdown.markdown
    html_str = converter(markdown_str)
    html_str = re.sub(r"&lt;", r"<", html_str)
    html_str = re.sub(r"&gt;", r">", html_str)
    return html_str

def markdown_str_to_dita_str(markdown_str, output_file):
    "Return a DITA string from a Markdown string."
    converter = markdown2dita.Markdown(title_level=4)
    random_id = "".join([random.choice(string.ascii_lowercase + string.digits) for n in range(8)])
    dita_str = converter(markdown_str)
    dita_str = re.sub("id=\"enter-id-here\"", f"id=\"{random_id}\"", dita_str)  # Adds a random ID to each topic
    dita_str = re.sub(">\n><", ">\n<", dita_str)    # Fixes a markdown2dita bug
    dita_str = re.sub(r"<shortdesc>Enter the short description for this page here</shortdesc>", "<shortdesc></shortdesc>", dita_str)    # Removes the hardcoded shortdesc
    dita_str = re.sub("<title>Enter the page title here</title>", f"<title>{output_file.replace('.dita', '')}</title>", dita_str)   # Replaces the title to match filename
    dita_str = re.sub("\n\n", "\n", dita_str)
    return dita_str

def html_str_to_dita_str(html_str, output_file):
    "Return a DITA string from an HTML string (with the use of Markdown as an intermediary format)."
    markdown_str = html_str_to_markdown_str(html_str)
    dita_str = markdown_str_to_dita_str(markdown_str, output_file)
    return dita_str

def html_str_to_markdown_str(html_str):
    "Return a Markdown String from an HTML string."
    converter = tomd.convert
    markdown_str = converter(html_str)
    markdown_str = re.sub(r"\n\s*\n\s*", "\n\n", markdown_str)
    return markdown_str

def convert_folder(source, input_extension, converter, output_folder, output_extension):
    """Convert files in a folder."""
    start_time = time.time()
    input_files_list = files_list(source, input_extension)
    files_number = len(input_files_list)
    if files_number == 0:
        raise Exception(f"No {input_extension.upper()} files found in {source}")
    part = 100 / files_number
    progress = 0
    pb(progress)
    for input_filepath in input_files_list:
        progress += part
        pb(int(progress))
        output_file = os.path.basename(re.sub(f".{input_extension}", f".{output_extension}", input_filepath, flags=re.IGNORECASE))
        output_str = converter(read_file(input_filepath), output_file)
        save_str_as_file(output_str, output_folder + "/" + output_file)
    elapsed_time = time.time() - start_time
    print(f"Converted {files_number} {input_extension.upper()} file(s) to {output_extension.upper()} in {round(elapsed_time, 3)} seconds.")
    
def convert_file(source, input_extension, converter, output_extension):
    """Convert a specific file."""
    start_time = time.time()
    pb(0)
    source_extension = file_extension(source)
    if input_extension.lower() != source_extension.lower():
        raise Exception(f"You selected a wrong file type. Please select a(n) {input_extension.upper()} file.")
    output_file = os.path.basename(re.sub(f".{input_extension}", f".{output_extension}", source, flags=re.IGNORECASE))
    output_folder = os.path.dirname(os.path.abspath(source))
    output_str = converter(read_file(source), output_file)
    save_str_as_file(output_str, output_folder + "/" + output_file)
    elapsed_time = time.time() - start_time
    pb(100)
    print(f"Converted one {input_extension.upper()} file to {output_extension.upper()} in {round(elapsed_time, 3)} seconds.")