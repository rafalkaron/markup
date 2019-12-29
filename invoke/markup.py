# coding: utf-8
__version__ = "0.5"
__author__ = "Rafał Karoń <rafalkaron@gmail.com.com>"

"""
    MarkUP (Codename: Insightful Broccoli)
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Convert Markdown to HTML5 or DITA.
    
    Uses: 
    - "mistune" to parse Markdown.
    - "markdown2dita" to convert Markdown to DITA.

    Upcoming features:
    - Multiline input support
    - Conversion to DITA
    - Defined output and source folder
    - CLI
    - GUI
"""

#Libraries
import mistune              #Markdown parser
import datetime             #Date and time
import os                   #OS interface to work with files on a lower level
from pathlib import Path    #Allows for Path subclass

#Global Variables
_md = mistune.Markdown()                                                                       #Abbreviation for misuse invocations
_timestamp = datetime.datetime.now()                                                           #Timestamp for files

_out_file = open("out_" +str(_timestamp.strftime("%d_%m_%y-%H-%M-%S")) + ".html", "w")         #Output file
_out_folder = Path("out")                                                                      #Output folder as a path (pathlib needed)
_out_folder_str = str(_out_folder)                                                             #Output folder as a string

_src_file = open("src_" +str(_timestamp.strftime("%d_%m_%y-%H-%M-%S")) + ".md", "w")           #Source file
_src_folder = Path("src")                                                                      #Source folder
_src_folder_str = str(_src_folder)

#Functions
def intro():
    print("Convert your Markdown files")                                          #Display introductory text

def feed():
    _input_type = input("Do you want to select a Markdown file? \n [Y] - Enables you to select the Markdown file that you want to convert. \n [N] - Enables you to write or paste Markdown syntax without the need to have a Markdown file. \n Enter [Y/N] ")
    if _input_type == "N" or _input_type == "n":
        new_md_to_html5()
    elif _input_type == "Y" or _input_type =="y":
        convert_md_to_html5()
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
    _input_text = '\n'.join(MultiLine)
    """

def new_md_to_html5():
    global _new_md_to_html5_called
    _new_md_to_html5_called = True #checks if the function was run
#Saves the output
    global _input_text
    _input_text = input("Enter Markdown syntax: ")
    _out_file.write(_md(_input_text))
    source_file()

_new_md_to_html5_called= False #checks if the function was not run

def convert_md_to_html5():
    global _convert_md_to_html5_called
    _convert_md_to_html5_called = True #checks if the function was run

    _file_location = input("Provide a full path to the Markdown file: ")
    _input_file = open(_file_location)
    _out_file.write(_md(_input_file.read()))

_convert_md_to_html5_called = False #checks if the function was not run

"""
def new_md_to_dita():


def convert_md_to_dita():
"""
def source_file():
    #Determines if you want to save the source file
    _save_source = input("Do you want to retain the Markdown source file? \n [Y] - Saves the Markdown file in the src folder. \n [N] - Discards the Markdown file. \n Enter [Y/N] ")
    if _save_source == "N" or _save_source == "n":
        print("The source Markdown file will not be saved.")
    elif _save_source == "Y" or _save_source =="y":
        source_folder()
        _src_file.write(_input_text)
        print("The source Markdown file will be saved in the " + _src_folder_str + " directory.")
    else: 
        print("Try answering the following question again by entering the \"Y\" or \"N\" characters withour quotation marks.")
        source_file()

def source_folder():
    if not os.path.exists(_src_folder):         #If the directory does not exist...
        os.mkdir(_src_folder)                   #Create the "src" directory in the script directory
        os.chdir(os.curdir/_src_folder)         #Changes the directory to the "src" directory

def out_folder():
    if not os.path.exists(_out_folder):         #If the directory does not exist...
        os.mkdir(_out_folder)                   #Create the "out" directory in the script directory
        os.chdir(os.curdir/_out_folder)         #Changes the directory to the "out" directory

def summary():
    if _new_md_to_html5_called == True:
        print("The Markdown syntax that you provided was rednered to the HTML5 file and put in the " + _out_folder_str + " folder.")
    elif _convert_md_to_html5_called == True:
        print("Your converted Markdown file was put to the " + _out_folder_str +" folder.")
    print("Thank you for using my software!")   #modify to display a raport

#Function calls
intro()
out_folder()
feed()
summary()
exit()