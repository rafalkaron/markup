# coding: utf-8
__author__ = "Rafał Karoń <rafalkaron@gmail.com>"

import markdown
from markdownify import markdownify
import mistune
import re

def markdown_str_to_html_str(markdown_str):
    html_str = markdown.markdown(markdown_str)
    return html_str

def markdown_str_to_dita_str(markdown_str):
    dita_str = mistune
    return dita_str

def html_str_to_markdown_str(html_str):
    markdown_str = markdownify(html_str)
    markdown_str = re.sub(r"\n\s*\n\s*", "\n\n", markdown_str)
    return markdown_str