__version__ = "0.1"
__author__ = "Rafał Karoń <rafalkaron@gmail.com.com>"

#Multiline string for multiline comments. This can be also used for multiline strings declarations
"""
    MarkUP (Codename: Flamingo Plumage)
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Batch-convert Markdown files to DITA by using markdown2dita script.
"""
#Import libraries
import mistune
import datetime

#Global Variables (must start with a letter or "_", only alphanumeric chars and underscores, case sensitive)
_md = mistune.Markdown()
_timestamp = datetime.datetime.now()
_output_folder = "/DITA"
_out_file = open("out_" +str(_timestamp.strftime("%d_%m_%y-%H-%M-%S")) + ".html", "w")

_out_file.write(_md("*testing out markdown parsing*"))

#Invokations
"""
def intro():            #A function
    _intro_text = "Marking up your Markdown files..."
    _no_time_msg = " We\'ll finish in no time." #This is a variable defined inside a function. It'll only work in the scope of the function. There can be global variable called like that, too. You can add global keyword to make the variable defined inside a function act as a global variable.
    print(_intro_text + _no_time_msg + " The converted files will be placed in the " + _output_folder + " folder.") #you can add multiple functions by using the + character
intro()
"""
# take all .md files from the current directory

"""
def read():
    f = open("SampleMarkdown.md", "rt")
    print(f.read())
read()
"""

# run the markdown2dita command against each file
# save the output in the DITA subfolder