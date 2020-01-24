#coding: utf-8
"""
    MarkUP Lite (Codename: Adolescent Flamingo)
    ****************************************************************

    Convert all Markdown files in the MarkUP Lite directory to DITA.
    
    ****************************************************************
    Dependencies:
    Uses "markdown2dita" to convert Markdown to DITA. 
    "markdown2dita" uses "misuse" to parse Markdown.
"""
#Markdown2dita Modules
from __future__ import print_function
import argparse, sys, mistune
#Markup Lite Modules
import os, glob, time, re

__version__ = "0.7"
__author__ = "Rafał Karoń <rafalkaron@gmail.com>"

#markdown2dita code
class Renderer(mistune.Renderer):

    def codespan(self, text):
        return '<codeph>{0}</codeph>'.format(escape(text.rstrip()))

    def link(self, link, title, content):
        return '<xref href="{0}">{1}</xref>'.format(link, escape(content or title))

    def block_code(self, code, language=None):
        code = escape(code.rstrip('\n'))
        if language:
            return ('<codeblock outputclass="language-{0}">{1}</codeblock>'
                    .format(language, code))
        else:
            return '<codeblock>{0}</codeblock>'.format(code)

    def block_quote(self, text):
        return '<codeblock>{0}</codeblock>'.format(text)

    def header(self, text, level, raw=None):
        # Dita only supports one title per section
        title_level = self.options.get('title_level', 2)
        if level <= title_level:
            return '</section><section><title>{0}</title>'.format(text)
        else:
            return '<p><b>{0}</b></p>'.format(text)

    def double_emphasis(self, text):
        return '<b>{0}</b>'.format(text)

    def emphasis(self, text):
        return '<i>{0}</i>'.format(text)

    def hrule(self):
        # Dita has no horizontal rule, ignore it
        # could maybe divide sections?
        return ''

    def inline_html(self, text):
        # Dita does not support inline html, just pass it through
        return text

    def list_item(self, text):
        return '<li>{0}</li>'.format(text)

    def list(self, body, ordered=True):
        if ordered:
            return '<ol>{0}</ol>'.format(body)
        else:
            return '<ul>{0}</ul>'.format(body)

    def image(self, src, title, text):

        # Derived from the mistune library source code

        src = mistune.escape_link(src)
        text = escape(text, quote=True)
        if title:
            title = escape(title, quote=True)
            output = ('<fig><title>{0}</title>\n'
                      '<image href="{1}" alt="{2}"/></fig>'
                      .format(title, src, text))
        else:
            output = '<image href="{0}" alt="{1}"/>'.format(src, text)

        return output

    def table(self, header, body, cols):
        col_string = ['<colspec colname="col{0}"/>'.format(x+1)
                      for x in range(cols)]
        output_str = ('<table>\n<tgroup cols="{0}">\n{1}\n'
                      .format(cols, '\n'.join(col_string)))

        return (output_str + '<thead>\n' + header + '</thead>\n<tbody>\n' +
                body + '</tbody>\n</tgroup>\n</table>')

    def table_row(self, content):
        return '<row>\n{0}</row>\n'.format(content)

    def table_cell(self, content, **flags):
        align = flags['align']

        if align:
            return '<entry align="{0}">{1}</entry>\n'.format(align, content)
        else:
            return '<entry>{0}</entry>\n'.format(content)

    def autolink(self, link, is_email=False):
        text = link = escape(link)
        if is_email:
            link = 'mailto:{0}'.format(link)
        return '<xref href="{0}">{1}</xref>'.format(link, text)

    def footnote_ref(self, key, index):
        return ''

    def footnote_item(self, key, text):
        return ''

    def footnotes(self, text):
        return ''

    def strikethrough(self, text):
        return text

class Markdown(mistune.Markdown):

    def __init__(self, renderer=None, inline=None, block=None, **kwargs):
        if not renderer:
            renderer = Renderer(**kwargs)
        else:
            kwargs.update(renderer.options)

        super(Markdown, self).__init__(
            renderer=renderer, inline=inline, block=block)

    def parse(self, text, page_id='enter-id-here',
              title='Enter the page title here'):
        output = super(Markdown, self).parse(text)

        if output.startswith('</section>'):
            output = output[9:]
        else:
            output = '<section>\n' + output

        output = """<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE concept PUBLIC "-//OASIS//DTD DITA Concept//EN" "concept.dtd">
<concept xml:lang="en-us" id="{0}">
<title>{1}</title>
<shortdesc>Enter the short description for this page here</shortdesc>
<conbody>
{2}</section>
</conbody>
</concept>""".format(page_id, title, output)
        return output

    def output_table(self):

        # Derived from the mistune library source code
        aligns = self.token['align']
        aligns_length = len(aligns)

        cell = self.renderer.placeholder()

        # header part
        header = self.renderer.placeholder()
        cols = len(self.token['header'])
        for i, value in enumerate(self.token['header']):
            align = aligns[i] if i < aligns_length else None
            flags = {'header': True, 'align': align}
            cell += self.renderer.table_cell(self.inline(value), **flags)

        header += self.renderer.table_row(cell)

        # body part
        body = self.renderer.placeholder()
        for i, row in enumerate(self.token['cells']):
            cell = self.renderer.placeholder()
            for j, value in enumerate(row):
                align = aligns[j] if j < aligns_length else None
                flags = {'header': False, 'align': align}
                cell += self.renderer.table_cell(self.inline(value), **flags)
            body += self.renderer.table_row(cell)

        return self.renderer.table(header, body, cols)


def escape(text, quote=False, smart_amp=True):
    return mistune.escape(text, quote=quote, smart_amp=smart_amp)

def _parse_args(args):
    parser = argparse.ArgumentParser(description='markdown2dita - a markdown '
                                     'to dita-ot CLI conversion tool.')
    parser.add_argument('-i', '--input-file',
                        help='input markdown file to be converted.'
                             'If omitted, input is taken from stdin.')
    parser.add_argument('-o', '--output-file',
                        help='output file for the converted dita content.'
                             'If omitted, output is sent to stdout.')
    return parser.parse_args(args)

def markdown(text, escape=True, **kwargs):
    return Markdown(escape=escape, **kwargs)(text)

#MarkUP Lite Global Variables
_markup_filepath = os.path.abspath(__file__)
_markup_filename = os.path.basename(__file__)
_markup_directory = _markup_filepath.replace(_markup_filename, "").replace("\\", "/")
_markdown_files = glob.glob(_markup_directory + "/*.md")
_markdown_files_uppercase = glob.glob(_markup_directory + "/*.MD")
_markdown_files_full = glob.glob(_markup_directory + "/*.markdown")
_markdown_files_full_uppercase = glob.glob(_markup_directory + "/*.MARKDOWN")
_markdown_files_all = list(set(_markdown_files + _markdown_files_uppercase + _markdown_files_full + _markdown_files_full_uppercase))

#MarkUP Lite code
def intro():
    print("Converting your Markdown files to DITA...")
"""
def convert():
    for _markdown_file in _markdown_files_all:
        os.system("markdown2dita -i " + "\"" + _markdown_file + "\"" + " -o " + "\"" + re.sub("md", "dita", _markdown_file, flags=re.IGNORECASE) + "\"")
"""

def convert():
    for _markdown_file in _markdown_files_all:
        input_str = open(_markdown_file, 'r').read()
        markdown = Markdown()
        dita_output = markdown(input_str)
        with open(re.sub(r"(\.md|\.markdown)", ".dita", _markdown_file, flags=re.IGNORECASE), "w") as output_file: #add to re.sub md or markdown
            output_file.write(dita_output)
     
def summary():
    print("Conversion successful!\nThis window will close automatically in 5 seconds.")
    time.sleep(5)

intro()
convert()
summary()