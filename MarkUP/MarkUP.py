# coding: utf-8
"""
    MarkUP Lite (Codename: Even Flamingo)
    ****************************************************************

    Convert all Markdown files in the MarkUP Lite directory to DITA.
    
    ****************************************************************
    Dependencies:
    Uses "markdown2dita" to convert Markdown to DITA. 
    "markdown2dita" uses "misuse" to parse Markdown.

    Coming soon:
    - Settable topictypes
    - MacOS version
    - CLI
    - File explorer?
    - The <title> tag should encapsulate the first #, the <abstract> tag should encapsulate what's under the first #
    - Program crashes if there's a file with markdown extension that actually contains the XML code (cannot be processed by the parser) - test out if that happens with codeblocks
    - Additional ">" characher after conbody is sometimes inserted
    - Set read-only to input files?
    - Error msg if sth goes wrong
    - Table in the console output
"""
from __future__ import print_function
import argparse, sys, mistune, os, glob, re, random, string, datetime
from xml.dom.minidom import parseString, xml

__version__ = "1.1"
__author__ = "Rafał Karoń <rafalkaron@gmail.com>"

# MarkUP Variables
## Markup executable location
_markup_filepath = os.path.abspath(__file__)
_markup_filename = os.path.basename(__file__)
_markup_directory = _markup_filepath.replace(_markup_filename, "").replace("\\", "/")
## Markdown files in the Markup location with different extensions
_md_files = glob.glob(_markup_directory + "/*.md")
_md_files_upper = glob.glob(_markup_directory + "/*.MD")
_markdown_files = glob.glob(_markup_directory + "/*.markdown")
_markdown_files_upper = glob.glob(_markup_directory + "/*.MARKDOWN")
### Aggregation of every Markup file in the Markup location
_markdown_files_all = list(set(_md_files + _md_files_upper + _markdown_files + _markdown_files_upper))
# Timestamps for logs
_timestamp = datetime.datetime.now()

class termcolor:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

# MarkUP Code
def intro():
    print(termcolor.GREEN + "Converting the following Markdown files from " + termcolor.UNDERLINE + _markup_directory + termcolor.END + termcolor.GREEN + " to DITA" + termcolor.END)

def convert():
    for _markdown_file in _markdown_files_all:
        _file_title = re.sub(r"(\.md|\.markdown)", "", _markdown_file, flags=re.IGNORECASE).replace("\\", "/")
        global _topic_id
        _topic_id = "topic_" + "".join([random.choice(string.ascii_lowercase + string.digits) for n in range(8)])
        _input_str = open(_markdown_file, 'r').read()
        
        class Markdown(mistune.Markdown):
            def __init__(self, renderer=None, inline=None, block=None, **kwargs):
                if not renderer:
                    renderer = Renderer(**kwargs)
                else:
                    kwargs.update(renderer.options)
                super(Markdown, self).__init__(
                    renderer=renderer, inline=inline, block=block)

            def parse(self, text, page_id = _topic_id,
                    title= _file_title.replace(_markup_directory, "")):
                output = super(Markdown, self).parse(text)
                if output.startswith('</section>'):
                    output = output[9:]
                else:
                    output = '<section>\n' + output
                output = """<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE concept PUBLIC "-//OASIS//DTD DITA Concept//EN" "concept.dtd">
<concept xml:lang="en-us" id="{0}">
<title>{1}</title>
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
        
        # Output
        _markdown = Markdown()
        _dita_output = _markdown(_input_str)
        _dita_output_parse = xml.dom.minidom.parseString(_dita_output)
        _dita_output_pretty = _dita_output_parse.toprettyxml(indent="\t", newl="\n")
        _dita_output_prettier = '\n'.join(list(filter(lambda x: len(x.strip()), _dita_output_pretty.split('\n'))))
        with open(re.sub(r"(\.md|\.markdown)", ".dita", _markdown_file, flags=re.IGNORECASE), "w") as output_file:
            output_file.write(_dita_output_prettier)

        # Logs
        global _log_converted
        _log_converted = (_markdown_file + " -> " + re.sub(r"(\.md|\.markdown)", ".dita", _markdown_file, flags=re.IGNORECASE)).replace("\\", "/")
        global _log_topic_id
        _log_topic_id =  _topic_id
        print(" - " + _log_converted.replace(_markup_directory, "") + " [@ID=" + _log_topic_id +"]")
        if _log_called == True:
            log_items()        

def log():
    global _log_called
    _log_called = True
    with open(_markup_directory + "/" + "log_markup.txt", "a") as log_file:
        log_file.write("Converted on " + str(_timestamp.strftime("%x")) + " at " + str(_timestamp.strftime("%X")) + "\n")
_log_called = False

def log_items():
    with open(_markup_directory + "/" + "log_markup.txt", "a+") as log_file:
        log_file.write(" - " + _log_converted + " [@ID=" + _log_topic_id +"]" + "\n")

def summary():
    if _log_called == False:
        print(termcolor.GREEN + "Conversion successful!" + termcolor.END) 
    if _log_called == True:
        print(termcolor.GREEN + "Conversion successful! For detailed information, see log_markup.txt" + termcolor.END)
    _exit_prompt = input(termcolor.BOLD + termcolor.YELLOW + "To exit, press [Enter]" + termcolor.END)
    if _exit_prompt:
        exit(0)

# markdown2dita code
class Renderer(mistune.Renderer):
    for _markdown_file in _markdown_files_all:
        global _topic_id
        _topic_id = "\"topic_" + "".join([random.choice(string.ascii_lowercase + string.digits) for n in range(8)]) + "\""
    
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
        return ''

    def inline_html(self, text):
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

# markdown2dita code
def escape(text, quote=False, smart_amp=True):
    return mistune.escape(text, quote=quote, smart_amp=smart_amp)

# Invocations
intro()
log()
convert()
summary()