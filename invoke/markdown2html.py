# coding: utf-8
__version__ = "0.3"
__author__ = "Rafał Karoń <rafalkaron@gmail.com.com>"

"""
    markdown2html (Codename: Voluptuous Broccoli)
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Convert Markdown to HTML5.
    *Uses "mistune" to parse the Markdown.

    Upcoming features:
    - Multiline input support
    - Conversion to DITA
    - Defined output folder
    - Retain Markdown input and put it in the src folder
    - CLI
    - GUI
"""

#Libraries
import mistune              #Markdown parser
import datetime             #Date and time
import os                   #OS interface to work with files on a lower level
from pathlib import Path    #Allows for Path subclass

#Global Variables
_md = mistune.Markdown()
_timestamp = datetime.datetime.now()
_out_file = open("out_" +str(_timestamp.strftime("%d_%m_%y-%H-%M-%S")) + ".html", "w")         #Output file
_out_folder = Path("out")                                                                      #Output folder as a path (pathlib needed)
_out_folder_str = str(_out_folder)                                                             #Output folder as a string

#Functions
def intro():
    print("Convert your Markdown files")                                          #Display introductory text

def feed():
    _input_type = input("Do you want to select a Markdown file? \n [Y] - Enables you to select the Markdown file that you want to convert. \n [N] - Enables you to write or paste Markdown syntax without the need to have a Markdown file. \n Enter [Y/N] ")
    if _input_type == "N" or _input_type == "n":
        new_file()
    elif _input_type == "Y" or _input_type =="y":
        load_file()
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

def new_file():
    global _new_file_called
    _new_file_called = True
    _input_text = input("Enter Markdown syntax: ")
    _out_file.write(_md(_input_text))
_new_file_called= False

def load_file():
    global _load_file_called
    _load_file_called = True
    _file_location = input("Provide a full path to the Markdown file: ")
    _input_file = open(_file_location)
    _out_file.write(_md(_input_file.read()))
_load_file_called = False

"""
def new_md_to_dita():


def convert_md_to_dita():
"""

def out_folder():
    if not os.path.exists(_out_folder):         #If the directory does not exist...
        os.mkdir(_out_folder)                   #Create the "out" directory in the script directory
        os.chdir(os.curdir/_out_folder)         #Changes the directory to the "out" directory

def summary():
    if _new_file_called == True:
        print("The Markdown syntax that you provided was rednered to the HTML5 file and put in the " + _out_folder_str + " folder.")
    elif _load_file_called == True:
        print("Your converted Markdown file was put to the " + _out_folder_str +" folder.")
    print("Thank you for using my software!")   #modify to display a raport

#Function calls
intro()
out_folder()
feed()
summary()
exit()