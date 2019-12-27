# coding: utf-8
__version__ = "0.2.1"
__author__ = "Rafał Karoń <rafalkaron@gmail.com.com>"

"""
    markdown2html (Codename: Asymetric Flamingo)
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Convert Markdown to HTML5.
    Uses mistune to parse the markdown.
"""
#Libraries
import mistune
import datetime

#Global Variables
_md = mistune.Markdown()
_timestamp = datetime.datetime.now()

def intro():
    print("Convert your Markdown files to HTML5.")

def feed():
    _input_type = input("Do you want to select a Markdown file? \n [Y] - Enables you to select the Markdown file that you want to convert. \n [N] - Enables you to write or paste Markdown syntax without the need to have a Markdown file. \n Enter [Y/N] ")
    if _input_type == "Y":
        load_file()
        exit()
    elif _input_type =="y":
        load_file()
        exit()
    if _input_type =="N":
        new_file()
        exit()
    elif _input_type =="n":
        new_file()
        exit()
    else:
        print("Try answering the following question again by entering the \"Y\" or \"N\" characters withour quotation marks.")
        feed()

def new_file():
    _input_text = input("Enter Markdown syntax: ")
    out()
    _out_file.write(_md(_input_text))
    exit()

def load_file():
    _file_location = input("Provide a full path to the Markdown file: ")
    _input_file = open(_file_location)
    out()
    _out_file.write(_md(_input_file.read()))

def out():
    global _out_file
    _out_file = open("out_" +str(_timestamp.strftime("%d_%m_%y-%H-%M-%S")) + ".html", "w")
    
#Function calls
intro()
feed()