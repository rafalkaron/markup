# coding: utf-8
__author__ = "Rafał Karoń <rafalkaron@gmail.com>"

import mistune
import markdown2dita
import tomd
import re
import uuid
import os
import logging
from lxml import etree
from .files import (read_file,
                    save_str_as_file,
                    files_list)

# Configure logger (file and console)
logging.basicConfig(filename=f"MarkUP.log",
                    format='%(asctime)s | %(message)s', filemode='w')
l = logging.getLogger()
l.setLevel(logging.INFO)
logging.getLogger().addHandler(logging.StreamHandler())


class Source:
    def __init__(self, source, conversion, output_dir=""):
        self.source = source
        self.conversion = conversion
        self.output_dir = output_dir

        # Determine if input is a dir or file
        if os.path.isfile(self.source):
            self.is_source_dir = False
        elif os.path.isdir(self.source):
            self.is_source_dir = True

        # Set the conversion type
        if conversion == "md_dita":
            self.source_extension = "md"
            self.output_extension = "dita"
        elif conversion == "html_dita":
            self.source_extension = "html"
            self.output_extension = "dita"
        elif conversion == "md_html":
            self.source_extension = "md"
            self.output_extension = "html"
        elif conversion == "html_md":
            self.source_extension = "html"
            self.output_extension = "md"
        else:
            raise Exception(
                f"{conversion} is not an allowed conversion type. Try entering: 'md_dita', 'html_dita', 'md_html', or 'html_md'")

    def convert(self):
        source_files_list = []
        output_files_list = []
        convert_all = False

        if self.is_source_dir == True:
            source_files_list = files_list(self.source, self.source_extension)

        elif self.is_source_dir == False:
            source_files_list = [self.source]

        for source_item in source_files_list:

            source_file_str = read_file(source_item)
            output_file = source_item.replace(
                f".{self.source_extension}", f".{self.output_extension}")
            output_filename = os.path.basename(output_file)

            # Determine the output dir
            if self.output_dir == "":
                output_filepath = output_file
            elif self.output_dir != "":
                output_filepath = f"{self.output_dir}/{output_filename}"
            if not os.path.exists(os.path.dirname(output_filepath)):
                os.makedirs(os.path.dirname(output_filepath))

            l.info(f"Converting {source_item} to {output_filepath}")

            if self.conversion == "md_dita":
                output_str = self.markdown_str_to_dita_str(
                    source_file_str, output_filename)
            elif self.conversion == "html_dita":
                output_str = self.html_str_to_dita_str(
                    source_file_str, output_filename)
            elif self.conversion == "md_html":
                output_str = self.markdown_str_to_html_str(source_file_str)
            elif self.conversion == "html_md":
                output_str = self.html_str_to_markdown_str(source_file_str)

            if os.path.isfile(output_filepath) and convert_all == False:
                prompt_overwrite = input(
                    f"Do you want to overwrite {output_filepath} [y/a/n]? ")

                if prompt_overwrite == "y" or prompt_overwrite == "Y":
                    l.info(f"Overwriting the {output_filepath} file")
                    output_file = save_str_as_file(output_str, output_filepath)
                    output_files_list.append(output_file)
                elif prompt_overwrite == "a" or prompt_overwrite == "A":
                    convert_all = True
                    l.info(
                        f"Overwriting all output files: {source_files_list}")
                    output_file = save_str_as_file(output_str, output_filepath)
                    output_files_list.append(output_file)
                elif prompt_overwrite == "n" or prompt_overwrite == "N":
                    l.info(f"Skipped the {output_filepath} file")
                else:
                    l.info(f"Exiting...")
                    break

            elif not os.path.isfile(output_filepath) or convert_all == True:
                output_file = save_str_as_file(output_str, output_filepath)
                output_files_list.append(output_file)

        return output_files_list

    @staticmethod
    def markdown_str_to_dita_str(markdown_str, output_filename) -> str:
        converter = markdown2dita.Markdown(title_level=4)
        dita_str = converter(markdown_str)
        dita_str = re.sub("id=\"enter-id-here\"",
                          f"id=\"concept-{uuid.uuid4()}\"", dita_str)
        dita_str = re.sub(">\n><", ">\n<", dita_str)
        dita_str = re.sub(r"<shortdesc>Enter the short description for this page here</shortdesc>",
                          "<shortdesc></shortdesc>", dita_str)    # Removes the hardcoded shortdesc
        dita_str = re.sub("<title>Enter the page title here</title>",
                          f"<title>{output_filename.replace('.dita', '')}</title>", dita_str)   # Replaces the title to match filename
        dita_str = re.sub("\n\n", "\n", dita_str)
        return dita_str

    @staticmethod
    def html_str_to_dita_str(html_str, output_filename) -> str:
        markdown_str = Source.html_str_to_markdown_str(html_str)
        dita_str = Source.markdown_str_to_dita_str(
            markdown_str, output_filename)
        return dita_str

    @staticmethod
    def markdown_str_to_html_str(markdown_str) -> str:
        html_str = mistune.markdown(markdown_str)
        html_str = re.sub(r"&lt;", r"<", html_str)
        html_str = re.sub(r"&gt;", r">", html_str)
        return html_str

    @staticmethod
    def html_str_to_markdown_str(html_str) -> str:
        markdown_str = tomd.convert(html_str)
        markdown_str = re.sub(r"\n\s*\n\s*", "\n\n", markdown_str)
        return markdown_str

    @staticmethod
    def pretty_print_html(self):
        pass
