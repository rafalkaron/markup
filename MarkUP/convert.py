# coding: utf-8
__author__ = "Rafał Karoń <rafalkaron@gmail.com>"

import markdown

def markdown_str_to_html_str(markdown_str):
    html_str = markdown.markdown(markdown_str)
    return html_str