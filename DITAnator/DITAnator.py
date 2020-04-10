# coding: utf-8
"""
    DITAnator
    ****************************************************************
    Batch-convert Markdown and HTML files to DITA.
    
    ****************************************************************
"""

from xml.dom.minidom import parseString, xml
import sys
import os
import mistune
import glob
import re
import random
import string
import datetime
import tomd
import markdown

__version__ = "0.1"
__author__ = "Rafał Karoń <rafalkaron@gmail.com>"

# The path of the script or executable
if getattr(sys, 'frozen', False):
    app_path = os.path.dirname(sys.executable)
elif __file__:
    app_path = os.path.dirname(__file__)
# The input directory defaults to the script or executable directory
in_dir = app_path
# The output directory defaults to the script or executable directory
out_dir = app_path

class Dirs:
    global try_again_msg
    try_again_msg = "Try answering the following question again by entering the \"Y\" or \"N\" characters without the quotation marks."

    @staticmethod
    def in_dir():
        print("The default input directory is: " + app_path)
        in_dir_set = input("Do you want to change the input directory?\n - To change the input directory, enter: Y\n - To keep the default input directory (" + app_path + ")" + ", enter: N\nAnswer: ")
        
        global in_dir
        if in_dir_set == "y" or in_dir_set =="Y":
            in_dir = input("Provide a full path to the directory that contains HTML5 and Markdown files that you want to convert: ").replace("\\", "/")
        elif in_dir_set == "n" or in_dir_set =="N":
            in_dir = app_path
        else:
            print(try_again_msg)
            Dirs.in_dir()
    
    def out_dir():
        print("the default output directory is: " + in_dir)
        out_dir_set = input("Do you want to change the input directory?\n - To change the input directory, enter: Y\n - To keep the default input directory (" + app_path + ")" + ", enter: N\nAnswer: ")
        
        global out_dir
        if out_dir_set == "y" or out_dir_set =="Y":
            out_dir = input("Provide a full path to the directory that contains HTML5 and Markdown files that you want to convert: ").replace("\\", "/")
        elif out_dir_set == "n" or out_dir_set =="N":
            out_dir = in_dir
        else:
            print(try_again_msg)
            Dirs.out_dir()

class SystemOutput:
    global log_file_path
    log_file_path = (in_dir + "/" + "log_markup.txt").replace("//", "/")
    parser_error_msg = " [File not pretty-printed due to parser error] "
    
    @staticmethod
    def dirs_info():
        # Terminal communicate indicating the source files directory
        print("Converting files to DITA from " + in_dir + " to " + out_dir)

    @staticmethod
    def report_html_to_md():
        # Terminal communicates listing the HTML source files and MD output files
        print("Converting HTML to Markdown:")
        print(" [+] " + in_html_file_name + " -> " + out_md_file_name)

    @staticmethod
    def report_md_to_dita():
        # Terminal communicates listing the MD source files, output files with IDs, and errors
        print("Converting Markdown to DITA:")
        if pretty_print == True:
            print(" [+] " + in_md_file_name + " -> " + out_dita_file_name + " @ID=" + dita_concept_id)
        if pretty_print == False:
            print(" [!] " + in_md_file_name + " -> " + out_dita_file_name + " @ID=" + dita_concept_id + parser_error_msg)
    
    @staticmethod
    def summary():
        # Terminal communicates summarising the conversion
        print("Conversion completed!") 
        if log_called == True:
            print("For detailed information, see: " + log_file_path)
        # Controls the OS-specific terminal behavior
        if os.name=="nt":
            exit_prompt = input("To finish, press [Enter]")
            if exit_prompt:
                exit(0)
        if os.name=="posix":
            exit(0)
    
    @staticmethod
    def log_init():
        timestamp = datetime.datetime.now()
        # Initializes a log file
        global log_called
        log_called = True
        # Creates a new log file or adds to the existing log file. Adds a timestamp.
        with open(log_file_path, "a+", encoding="utf-8") as log_file:
            log_file.write("Conversion started on " + str(timestamp.strftime("%x")) + " at " + str(timestamp.strftime("%X")) + "\n" + " [i] Input directory: " + in_dir + "\n" + " [o] Output directory: " + out_dir +"\n")
    log_called = False

    @staticmethod
    def log_html_to_md():
        # Writes to the initialized log file
        with open(log_file_path, "a+", encoding ="utf-8") as log_file:
            # Log items listing the source files, output files with IDs, and errors
            log_file.write(" [+] " + in_html_file_name + " -> " + out_md_file_name + "\n")

    @staticmethod
    def log_md_to_dita():
        # Writes to the initialized log file
        with open(log_file_path, "a+", encoding ="utf-8") as log_file:
            if pretty_print == True:
                log_file.write(" [+] " + in_md_file_name + " -> " + out_dita_file_name + " @ID=" + dita_concept_id + "\n")
            if pretty_print == False:
                log_file.write(" [!] " + in_md_file_name + " -> " + out_dita_file_name + " @ID=" + dita_concept_id + parser_error_msg + "\n")

class Converter:
    def html_to_md():                                                       # Will need to replace app_file with another variable when the directory picker is added to the code
        # Lists the HTML files in the source directory
        html_files_lower = glob.glob(in_dir + "/*.html")
        html_files_upper = glob.glob(in_dir + "/*.HTML")
        html_files = list(set(html_files_lower + html_files_upper))

        for html_file in html_files:
        # Variables
            global in_html_file_path
            in_html_file_path = html_file.replace("\\", "/")
            global in_html_file_name
            in_html_file_name = in_html_file_path.replace(in_dir + "/", "").replace(in_dir, "")
            global out_md_file_name
            out_md_file_name = re.sub(r".html", ".md", in_html_file_name, flags=re.IGNORECASE)
            global out_md_file_path
            out_md_file_path = out_dir + "/" + out_md_file_name
        # Input
            html_str = open(html_file, 'r').read()
            # Pretty-prints HTML prior to conversion
            html_str_pretty = '\n'.join(list(filter(lambda x: len(x.strip()), html_str.split('\n'))))
        # Conversion
            convert_tomd = tomd.convert(html_str_pretty)
        # Output
            with open(out_md_file_path, "w") as md_output:
                # Pretty-print HTML output
                md_prettish = re.sub(r"[ \t]+", " ", convert_tomd)
                md_pretty = re.sub(r"\n\s*\n\s*", "\n\n", md_prettish)
                md_output.write(md_pretty)
        # Logging
            if log_called == True:
                SystemOutput.log_html_to_md()
        # Terminal feedback
            SystemOutput.report_html_to_md()

    def md_to_dita():
        # Lists the MD files in the source directory
        md_files_lower = glob.glob(in_dir + "/*.md")
        md_files_upper = glob.glob(in_dir + "/*.MD")
        markdown_files_lower = glob.glob(in_dir + "/*.markdown")
        markdown_files_upper = glob.glob(in_dir + "/*.MARKDOWN")
        md_files = list(set(md_files_lower + md_files_upper + markdown_files_lower + markdown_files_upper))
        
        for md_file in md_files:
        # Variables
            global in_md_file_path
            in_md_file_path = md_file.replace("\\", "/")
            global in_md_file_name
            in_md_file_name = in_md_file_path.replace(in_dir + "/", "").replace(in_dir, "")
            global in_md_file_title
            in_md_file_title = re.sub(r"(\.md|\.markdown)", "", in_md_file_name, flags=re.IGNORECASE)
            global dita_concept_id
            dita_concept_id = "concept_" + "".join([random.choice(string.ascii_lowercase + string.digits) for n in range(8)])
            global out_dita_file_name
            out_dita_file_name = re.sub(r"(\.md|\.markdown)", ".dita", in_md_file_name, flags=re.IGNORECASE)
            global out_dita_file_path
            out_dita_file_path = out_dir + "/" + out_dita_file_name
        # Input
            md_str = open(md_file, 'r').read()
        # Conversion
            class XML(mistune.Markdown):
                def __init__(self, renderer=None, inline=None, block=None, **kwargs):
                    if not renderer:
                        renderer = Renderer(**kwargs)
                    else:
                        kwargs.update(renderer.options)
                    super(XML, self).__init__(
                        renderer=renderer, inline=inline, block=block)
                def parse(self, text, page_id = dita_concept_id,
                        title= in_md_file_title):
                    output = super(XML, self).parse(text)
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
            _render = XML()
            _dita_output = _render(md_str)
            # Output
            with open(out_dita_file_path, "w") as output_file:
                try:
                    _dita_output_parse = xml.dom.minidom.parseString(_dita_output)
                    _dita_output_pretty = _dita_output_parse.toprettyxml(indent="\t", newl="\n")
                    _dita_output_prettier = '\n'.join(list(filter(lambda x: len(x.strip()), _dita_output_pretty.split('\n'))))
                    output_file.write(_dita_output_prettier)
                    global pretty_print
                    pretty_print = True
                except xml.parsers.expat.ExpatError:
                    output_file.write(_dita_output)
                    pretty_print = False
            # Logging
            if log_called == True:
                SystemOutput.log_md_to_dita()
            # Terminal Feedback
            SystemOutput.report_md_to_dita()

# This is needed to convert MD
def escape(text, quote=False, smart_amp=True):
    return mistune.escape(text, quote=quote, smart_amp=smart_amp)

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

def main():
    Dirs.in_dir()
    Dirs.out_dir()
    SystemOutput.dirs_info()
    SystemOutput.log_init() # Initializes the log file prior to running the converters
    Converter.html_to_md()
    Converter.md_to_dita()
    SystemOutput.summary()

if __name__ == '__main__':
    main()