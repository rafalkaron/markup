# coding: utf-8
__author__ = "Rafał Karoń <rafalkaron@gmail.com>"

def progressbar(percent, length=50, prefix="Converting", fill="#", empty="-"):
    """Print a progress bar.

    Keyword arguments:
    percent -- The integer that signifies the progress percent in the progress bar
    length -- The length of the progress bar
    prefix -- The text that precedes the progress bar (default \"Processing\")
    fill -- The characters that signifies the progress in the progress bar (default \"#\")
    empty -- The characters that signifies the empty space in the progress bar (default \" \")
    """
    fill = "".join([fill for _ in range(int(length*(percent/100)))])
    empty = "".join([empty for _ in range(int(length-length*(percent/100)))])
    bar = f"{prefix} [{fill}{empty}] {percent}%"
    if percent < 100:
        print(bar, end="\r", flush="true")
    if percent == 100:
        print(bar)