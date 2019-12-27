__version__ = "0.1"
__author__ = "Rafał Karoń <rafalkaron@gmail.com.com>"

"""
    markdown2html (Codename: Vain Flamingo)
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
intro()

def out():
#Function Variables
    _input_text = input("Enter Markdown syntax: ")
    _out_file = open("out_" +str(_timestamp.strftime("%d_%m_%y-%H-%M-%S")) + ".html", "w")
#Invocations
    _out_file.write(_md(_input_text)) #creates HTML5 from the MD syntax that you entered.
out()