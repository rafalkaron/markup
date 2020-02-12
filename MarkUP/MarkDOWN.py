# coding: utf-8
"""
    MarkDOWN (Codename: )
    ****************************************************************

    Convert all HTML files to MD
    
    ****************************************************************    
"""
import argparse, sys, mistune, os, glob, re, string
import tomd
import htmlmin

__version__ = "0.1"
__author__ = "Rafał Karoń <rafalkaron@gmail.com>"

if os.name=="nt":
    _script_filepath = os.path.abspath(__file__)
    _script_filename = os.path.basename(__file__)
    _script_directory = _script_filepath.replace(_script_filename, "").replace("\\", "/")
    _html_files = glob.glob(_script_directory + "/*.html")
    _html_files_upper = glob.glob(_script_directory + "/*.HTML")
    
if os.name=="posix":
    _script_directory = input("Enter a full path to the directory that contains the HTML files that you want to convert: ").replace("\\", "/").replace("//", "/")
    _md_files = glob.glob(_script_directory + "/*.html")
    _md_files_upper = glob.glob(_script_directory + "/*.HTML")

_html_files_all = list(set(_html_files + _html_files_upper))

def html_to_dita():
    for _html_file in _html_files_all:
    #Variables
        _in_file_path = _html_file.replace("\\", "/")
        _in_file_name = _in_file_path.replace(_script_directory + "/", "").replace(_script_directory, "")
        _out_file_path = re.sub(r".html", ".md", _in_file_path, flags=re.IGNORECASE)
        _out_file_name = _out_file_path.replace(_script_directory + "/", "").replace(_script_directory, "")
    #Input
        _input_str = open(_html_file, 'r').read()
        _input_mini = htmlmin.minify(_input_str, remove_empty_space=True)
    #Conversion
        _tomd = tomd.convert(_input_mini)
    #Output
        with open(_out_file_path, "w") as output_file:
            output_file.write(_tomd)



html_to_dita()
