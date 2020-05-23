# coding: utf-8
__author__ = "Rafał Karoń <rafalkaron@gmail.com>"

from markdownify import markdownify
import mistune
import markdown2dita
import tomd
import re

def markdown_str_to_html_str(markdown_str):
    html_str = mistune.markdown(markdown_str).replace("&lt;", "<").replace("&gt;", ">")
    return html_str

def markdown_str_to_dita_str(markdown_str):
    markdown = markdown2dita.Markdown(title_level=4)
    dita_str = markdown(markdown_str)
    return dita_str

def html_str_to_dita_str(html_str):
    pass

def html_str_to_markdown_str(html_str):
    #markdown_str = markdownify(html_str)
    markdown_str = tomd.convert(html_str)
    markdown_str = re.sub(r"\n\s*\n\s*", "\n\n", markdown_str)
    return markdown_str