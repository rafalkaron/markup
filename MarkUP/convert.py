# coding: utf-8
__author__ = "Rafał Karoń <rafalkaron@gmail.com>"

import markdown
import tomd
import mistune

def markdown_str_to_html_str(markdown_str):
    html_str = markdown.markdown(markdown_str)
    return html_str

def markdown_str_to_dita_str(markdown_str):
    dita_str = mistune
    return dita_str

def html_str_to_markdown_str(html_str):
    markdown_str = tomd
    return 