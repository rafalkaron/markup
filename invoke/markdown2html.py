__version__ = "0.1"
__author__ = "Rafał Karoń <rafalkaron@gmail.com.com>"

"""
    markdown2html (Codename: Vain Flamingo)
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Convert Markdown to HTML5.
"""
#Import Libraries
import mistune
import datetime

#Global Variables
_md = mistune.Markdown()
_timestamp = datetime.datetime.now()
_output_folder = "/DITA"
"""
def feed():
#Function Variables

    print(_input_text)
feed()
"""

def out():
#Function Variables
    _input_text = input("Enter Markdown syntax: ")
    _out_file = open("out_" +str(_timestamp.strftime("%d_%m_%y-%H-%M-%S")) + ".html", "w")
#Invocations
    _out_file
    _out_file.write(_md(_input_text))
out()