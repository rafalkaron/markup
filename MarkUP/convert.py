# coding: utf-8
__author__ = "Rafał Karoń <rafalkaron@gmail.com>"

import mistune
import markdown2dita
import tomd
import re
import uuid
import time
import os
from .files import read_file, save_str_as_file, files_list, file_extension

def markdown_str_to_html_str(markdown_str, output_file):
    """Return an HTML string from a Markdown string."""
    html_str = mistune.markdown(markdown_str)
    html_str = re.sub(r"&lt;", r"<", html_str)
    html_str = re.sub(r"&gt;", r">", html_str)
    return html_str

def markdown_str_to_dita_str(markdown_str, output_file):
    """Return a DITA string from a Markdown string."""
    converter = markdown2dita.Markdown(title_level=4)
    dita_str = converter(markdown_str)
    dita_str = re.sub("id=\"enter-id-here\"", f"id=\"concept-{uuid.uuid4()}\"", dita_str)
    dita_str = re.sub(">\n><", ">\n<", dita_str)    # Fixes a markdown2dita bug
    dita_str = re.sub(r"<shortdesc>Enter the short description for this page here</shortdesc>", "<shortdesc></shortdesc>", dita_str)    # Removes the hardcoded shortdesc
    dita_str = re.sub("<title>Enter the page title here</title>", f"<title>{output_file.replace('.dita', '')}</title>", dita_str)   # Replaces the title to match filename
    dita_str = re.sub("\n\n", "\n", dita_str)
    return dita_str

def html_str_to_dita_str(html_str, output_file):
    """Return a DITA string from an HTML string (with the use of Markdown as the intermediary format)."""
    markdown_str = html_str_to_markdown_str(html_str, output_file)
    dita_str = markdown_str_to_dita_str(markdown_str, output_file)
    return dita_str

def html_str_to_markdown_str(html_str, output_file):
    """Return a Markdown String from an HTML string."""
    markdown_str = tomd.convert(html_str)
    markdown_str = re.sub(r"\n\s*\n\s*", "\n\n", markdown_str)
    return markdown_str

def convert_folder(source, source_extension, converter, output_dir, output_extension):
    """Convert files in a folder."""
    elapsed_time = 0
    input_files = files_list(source, source_extension)
    files_number = len(input_files)
    existing_files = []
    if files_number == 0:
        raise Exception(f" [!] No {source_extension.upper()} files found in {source}")

    for input_filepath in input_files:
        output_file = os.path.basename(re.sub(f".{source_extension}", f".{output_extension}", input_filepath, flags=re.IGNORECASE))
        output_filepath = output_dir + "/" + output_file
        if os.path.isfile(output_filepath):
            existing_files.append(output_filepath)
    existing_files_str = "\n".join(existing_files)
    existing_files_str = "     * " + existing_files_str.replace("\n", "\n     * ")
    if len(existing_files) > 0:
        prompt = input(f" [?] Do you want to overwrite the following files? [y/n]\n{existing_files_str}\n [>] ")
        if prompt == "y" or prompt == "Y":
            pass
        elif prompt != "y" or prompt != "Y":
            print(" [i] Cancelled conversion.")
            return False

    for input_filepath in input_files:
        start_time = time.time()
        output_file = os.path.basename(re.sub(f".{source_extension}", f".{output_extension}", input_filepath, flags=re.IGNORECASE))
        output_filepath = output_dir + "/" + output_file
        output_str = converter(read_file(input_filepath), output_file)
        save_str_as_file(output_str, output_filepath)
        iter_time = time.time() - start_time
        elapsed_time = elapsed_time + iter_time
        print(f" [+] Converted {input_filepath} to {output_filepath}")
    print(f" [✔] Converted {files_number} {source_extension.upper()} file(s) to {output_extension.upper()} in {round(elapsed_time, 3)} seconds.")
    return True

def convert_file(source, source_extension, converter, output_dir, output_extension):
    """Convert a specific file."""
    source_extension = file_extension(source)
    if source_extension.lower() != source_extension.lower():
        raise Exception(f" [!] You selected a wrong file type. Please select a(n) {source_extension.upper()} file.")
    output_file = os.path.basename(re.sub(f".{source_extension}", f".{output_extension}", source, flags=re.IGNORECASE))
    output_filepath = output_dir + "/" + output_file
    output_filepath = output_filepath.replace("//", "/")
    if os.path.isfile(output_filepath):
        prompt = input(f" [?] Do you want to overwrite {output_filepath}? [y/n]: ")
        if prompt == "y" or prompt == "Y":
            pass
        elif prompt != "y" or prompt != "Y":
            print(" [i] Cancelled conversion.")
            return False
    start_time = time.time()
    output_str = converter(read_file(source), output_file)
    save_str_as_file(output_str, output_filepath)
    elapsed_time = time.time() - start_time
    print(f" [✔] Converted {source} to {output_filepath} in {round(elapsed_time, 3)} seconds.")
    return True

def md_html(source, output_dir):
    """Convert Markdown to HTML."""
    if os.path.isfile(source):
        convert_file(source, "md", markdown_str_to_html_str, output_dir, "html")
    elif os.path.isdir(source):
        convert_folder(source, "md", markdown_str_to_html_str, output_dir, "html")
    else:
        raise Exception(f" [!] {source} does not exist.")

def md_dita(source, output_dir):
    """Convert Markdown to DITA."""
    if os.path.isfile(source):
        convert_file(source, "md", markdown_str_to_dita_str, output_dir, "dita")
    elif os.path.isdir(source):
        details = convert_folder(source, "md", markdown_str_to_dita_str, output_dir, "dita")
    else:
        raise Exception(f" [!] {source} does not exist.")

def html_dita(source, output_dir):
    """Convert HTML to DITA."""
    if os.path.isfile(source):
        convert_file(source, "html", html_str_to_dita_str, output_dir, "dita")
    elif os.path.isdir(source):
        convert_folder(source, "html", html_str_to_dita_str, output_dir, "dita")
    else:
        raise Exception(f" [!] {source} does not exist.")

def html_md(source, output_dir):
    """Convert Markdown to DITA."""
    if os.path.isfile(source):
        convert_file(source, "html", html_str_to_markdown_str, output_dir, "md")
    elif os.path.isdir(source):
        convert_folder(source, "html", html_str_to_markdown_str, output_dir, "md")
    else:
        raise Exception(f" [!] {source} does not exist.")