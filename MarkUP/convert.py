# coding: utf-8
__author__ = "Rafał Karoń <rafalkaron@gmail.com>"

import mistune
import markdown2dita
import tomd
import re
import random
import string

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