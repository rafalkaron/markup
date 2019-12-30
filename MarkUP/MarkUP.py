# coding: utf-8
__version__ = "0.7"
__author__ = "Rafał Karoń <rafalkaron@gmail.com.com>"

"""
    MarkUP (Codename: Structured Broccoli)
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Convert Markdown to HTML5 or DITA.
    
    Uses: 
    - "mistune" to parse Markdown.
    - "markdown2dita" to convert Markdown to DITA.

    Upcoming features:
    - Multiline input support
    - CLI
    - GUI
"""

#Libraries
import mistune              #Markdown parser
import datetime             #Date and time
import os                   #OS interface to work with files on a lower level
from pathlib import Path    #Allows for Path subclass
import shutil               #Needed to remove files in the tmp folder

#Global Variables
_md = mistune.Markdown()
_timestamp = datetime.datetime.now()
_out_folder = Path("out")
_out_folder_str = str(_out_folder)    
_src_folder = Path("src")
_src_folder_str = str(_src_folder)
_tmp_folder = Path("tmp")
_tmp_folder_str = str(_tmp_folder)

#Functions
def intro():
    print("Convert your Markdown files")                                          #Display introductory text

def feed():
    _input_type = input("Do you want to select a Markdown file? \n [Y] - Enables you to select the Markdown file that you want to convert. \n [N] - Enables you to write or paste Markdown syntax without the need to have a Markdown file. \n Enter [Y/N] ")
    if _input_type == "N" or _input_type == "n":
        new_md_to_html5()
    elif _input_type == "Y" or _input_type =="y":
        convert_md_to_html5()
    elif _input_type == "md2dita":
        convert_md_to_dita()
    elif _input_type == "newmd2dita":
        new_md_to_dita()
    else: 
        print("Try answering the following question again by entering the \"Y\" or \"N\" characters withour quotation marks.")
        feed()
   
    """
def multiline():

    MultiLine = []
    while True:
        line = input()
    if line:
        MultiLine.append(line)
    else:
        break
    _md_input = '\n'.join(MultiLine)
    """

def convert_md_to_html5():
    global _convert_md_to_html5_called
    _convert_md_to_html5_called = True #checks if the function was run
    _file_location = input("Provide a full path to the Markdown file: ")
    _input_file = open(_file_location)
    out_html5()
    _out_html5.write(_md(_input_file.read()))
    _out_html5.close
_convert_md_to_html5_called = False #checks if the function was not run

def convert_md_to_dita():
    global _convert_md_to_dita_called
    _convert_md_to_dita_called = True
    _file_location = input("Provide a full path to the Markdown file: ")
    _md_to_dita = os.system("markdown2dita -i " + _file_location + " -o " + _out_folder_str + "/" + "out_" +str(_timestamp.strftime("%d_%m_%y-%H-%M-%S")) + ".dita")
_new_md_to_dita_called = False

def new_md_to_html5():
    global _new_md_to_html5_called
    _new_md_to_html5_called = True #checks if the function was run
    md_input()
    out_html5()
    _out_html5.write(_md(_md_input))
    _out_html5.close
    src_file()
_new_md_to_html5_called = False #checks if the function was not run

def new_md_to_dita():
    global _new_md_to_dita_called
    _new_md_to_dita_called = True
    tmp_folder()
    md_input()
    _tmp_file = open(_tmp_folder_str + "/" + "tmp.md", "w")
    _tmp_file.write(_md(_md_input))
    _md_to_dita = os.system("markdown2dita -i " + _tmp_folder_str + "/" + "tmp.md" + " -o " + _out_folder_str + "/" + "out_" +str(_timestamp.strftime("%d_%m_%y-%H-%M-%S")) + ".dita")
    src_file()
_new_md_to_dita_called = False

def tmp_folder():
    if not os.path.exists(_tmp_folder):
        os.mkdir(_tmp_folder)    

def tmp_folder_del():
    if os.path.exists(_tmp_folder):
        shutil.rmtree(_tmp_folder)

def src_file():
    #Determines if you want to save the source file
    _save_source = input("Do you want to retain the Markdown source file? \n [Y] - Saves the Markdown file in the src folder. \n [N] - Discards the Markdown file. \n Enter [Y/N] ")
    if _save_source == "N" or _save_source == "n":
        print("The source Markdown file will not be saved.")
    elif _save_source == "Y" or _save_source =="y":
        global _src_file
        _src_file = open(_src_folder_str + "/" + "src_" +str(_timestamp.strftime("%d_%m_%y-%H-%M-%S")) + ".md", "w")
        _src_file.write(_md_input)
        _src_file.close
        print("The source Markdown file will be saved in the " + _src_folder_str + " directory.")
    else: 
        print("Try answering the following question again by entering the \"Y\" or \"N\" characters withour quotation marks.")
        src_file()

def md_input():
    global _md_input
    _md_input = input("Enter Markdown: ")

def src_folder():
    if not os.path.exists(_src_folder):         #If the directory does not exist...
        os.mkdir(_src_folder)                   #Create the "src" directory in the script directory

def out_html5():
    global _out_html5
    _out_html5 = open(_out_folder_str + "/" + "out_" +str(_timestamp.strftime("%d_%m_%y-%H-%M-%S")) + ".html", "w")

def out_folder():
    if not os.path.exists(_out_folder):         #If the directory does not exist...
        os.mkdir(_out_folder)                   #Create the "out" directory in the script directory

def summary():
    if _new_md_to_html5_called == True:
        print("The Markdown syntax that you provided was rednered to the HTML5 file and put in the " + _out_folder_str + " folder.")
    elif _convert_md_to_html5_called == True:
        print("Your converted Markdown file was put to the " + _out_folder_str +" folder.")
    print("Thank you for using my software!")

#Function calls
intro()
out_folder()
src_folder()
feed()
summary()
tmp_folder_del()
exit()