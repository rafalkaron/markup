__version__ = "0.1"
__author__ = "Rafał Karoń <rafalkaron@gmail.com.com>"

#Multiline string for multiline comments
"""
    MarkUP (Codename: Flamingo Plumage)
    Batch-convert Markdown files to DITA by using markdown2dita script.
"""

#Variables (must start with a letter or "_", only alphanumeric chars and underscores, case sensitive)
_intro_text = "Marking up your Markdown files..."
_output_folder = "/DITA"


#Invokations

def intro():            #A function
    _no_time_msg = " We\'ll finish in no time." #This is a variable defined inside a function. It'll only work in the scope of the function. There can be global variable called like that, too.
    print(_intro_text + _no_time_msg + " The converted files will be placed in the " + _output_folder + " folder.") #you can add multiple functions by using the + character
intro()

# take all .md files from the current directory
# run the markdown2dita command against each file
# save the output in the DITA subfolder