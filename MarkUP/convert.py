# coding: utf-8
__author__ = "Rafał Karoń <rafalkaron@gmail.com>"

import mistune
import markdown2dita
import tomd
import re
import uuid
import time
import os
from .files import (read_file,
                    save_str_as_file,
                    files_list,
                    file_extension,
                    boolean_prompt)


class Source:
    def __init__(self, source, conversion, output_dir=""):
        self.source = source
        self.conversion = conversion
        self.output_dir = output_dir

        # Determine if input is a dir or file
        if os.path.isfile(source):
            self.is_source_dir = False
        elif os.path.isdir(source):
            self.is_source_dir = True

        # Set the output dir (defaults to the input dir)
        if self.output_dir == "":
            if self.is_source_dir == False:
                self.output_dir = os.path.dirname(source)
            elif self.is_source_dir == True:
                self.output_dir = source

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

        if self.is_source_dir == True:
            source_files_list = files_list(self.source, self.source_extension)
            print(source_files_list)

        elif self.is_source_dir == False:
            source_files_list = source_files_list.append(self.source)
            print(source_files_list)

        for source_file in source_files_list:
            source_file_str = read_file(source_file)
            output_file = source_file.replace(
                self.source_extension, self.output_extension)
            output_filename = os.path.basename(output_file)
            output_filepath = f"{self.output_dir}/{output_filename}"

            if os.path.isfile(output_filepath):
                boolean_prompt(
                    f" [?] Do you want to overwrite {output_filepath}? [y/n]: ")

            if self.conversion == "md_dita":
                output_str = self.markdown_str_to_dita_str(source_file_str)
            elif self.conversion == "html_dita":
                output_str = self.html_str_to_dita_str(source_file_str)
            elif self.conversion == "md_html":
                output_str = self.markdown_str_to_html_str(source_file_str)
            elif self.conversion == "html_md":
                output_str = self.html_str_to_markdown_str(source_file_str)

            return save_str_as_file(output_str, output_filepath)

    @staticmethod
    def markdown_str_to_dita_str(markdown_str) -> str:
        converter = markdown2dita.Markdown(title_level=4)
        dita_str = converter(markdown_str)
        dita_str = re.sub("id=\"enter-id-here\"",
                          f"id=\"concept-{uuid.uuid4()}\"", dita_str)
        # Fixes a markdown2dita bug
        dita_str = re.sub(">\n><", ">\n<", dita_str)
        dita_str = re.sub(r"<shortdesc>Enter the short description for this page here</shortdesc>",
                          "<shortdesc></shortdesc>", dita_str)    # Removes the hardcoded shortdesc
        # dita_str = re.sub("<title>Enter the page title here</title>",
        #                  f"<title>{output_file.replace('.dita', '')}</title>", dita_str)   # Replaces the title to match filename
        dita_str = re.sub("\n\n", "\n", dita_str)
        return dita_str

    @staticmethod
    def html_str_to_dita_str(html_str) -> str:
        markdown_str = Source.html_str_to_markdown_str(html_str)
        dita_str = Source.markdown_str_to_dita_str(markdown_str)
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

    def pretty_print(self):
        pass

    """
    def convert_file(self, source, converter, output_extension):
        output_file = os.path.basename(re.sub(
            f".{self.source_extension}", f".{output_extension}", source, flags=re.IGNORECASE))
        output_filepath = self.output_dir + "/" + output_file
        if os.path.isfile(output_filepath):
            boolean_prompt(
                f" [?] Do you want to overwrite {output_filepath}? [y/n]: ")
        start_time = time.time()
        output_str = converter(read_file(source), output_file)
        save_str_as_file(output_str, output_filepath)
        elapsed_time = time.time() - start_time
        print(
            f" [i] Converted {source} to {output_filepath} in {round(elapsed_time, 3)} seconds.")
        return output_filepath

    def convert_folder(self, source, source_extension, converter, output_dir, output_extension):
        elapsed_time = 0
        input_files = files_list(source, source_extension)
        files_number = len(input_files)
        existing_files = []
        if files_number == 0:
            raise Exception(
                f" [!] No {source_extension.upper()} files found in {source}")

        for input_filepath in input_files:
            output_file = os.path.basename(re.sub(
                f".{source_extension}", f".{output_extension}", input_filepath, flags=re.IGNORECASE))
            output_filepath = output_dir + "/" + output_file
            if os.path.isfile(output_filepath):
                existing_files.append(output_filepath)
        existing_files_str = "\n".join(existing_files)
        existing_files_str = "     * " + \
            existing_files_str.replace("\n", "\n     * ")
        if len(existing_files) > 0:
            boolean_prompt(
                f" [?] Do you want to overwrite the following files? [y/n]\n{existing_files_str}\n [>] ")
        for input_filepath in input_files:
            start_time = time.time()
            output_file = os.path.basename(re.sub(
                f".{source_extension}", f".{output_extension}", input_filepath, flags=re.IGNORECASE))
            output_filepath = output_dir + "/" + output_file
            output_str = converter(read_file(input_filepath), output_file)
            save_str_as_file(output_str, output_filepath)
            iter_time = time.time() - start_time
            elapsed_time = elapsed_time + iter_time
            print(f" [+] Converted {input_filepath} to {output_filepath}")
        print(
            f" [i] Converted {files_number} {source_extension.upper()} file(s) to {output_extension.upper()} in {round(elapsed_time, 3)} seconds.")
        return True
"""
