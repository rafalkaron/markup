
# MarkUP

Batch-convert Markdown and HTML files.

## Before you begin
1. Download the newest **MarkUP** version. See [Download MarkUP](https://github.com/rafalkaron/MarkUP/releases/latest).
2. Unzip **MarkUP**.

## Usage
1. In a terminal app, run: `markup <source> <conversion_type> --output <output_dir>`  
    Where:
    * **&lt;source&gt;** (required) is the file or directory that contains files that you want to convert.
    * **&lt;conversion_type&gt;** (required) is one of the following:
        * `md_dita` - converts Markdown to DITA
        * `html_dita` - converts HTML to DITA
        * `md_html` - converts Markdown to HTML
        * `html_md` - converts HTML to Markdown
    * **--output** or **-out** (optional) precedes the directory where you want to save the converted files.  
    **TIP:** By default the output directory is the same as the input directory.
2. If needed, accept any security prompt. For more information, see [Accepting macOS Security Prompts](https://github.com/rafalkaron/MarkUP/wiki/Accepting-macOS-Security-Prompts) or [Accepting Windows Security Prompts](https://github.com/rafalkaron/MarkUP/wiki/Accepting-Windows-Security-Prompts)

## Examples

The following converts every Markdown file to DITA in the `Downloads` directory.
```
MarkUP "/Users/user_name/Downloads" md_dita
```
The following coverts the `README.html` file to DITA in the `Desktop` directory.
```
MarkUP "/Users/user_name/Desktop/README.html" html_dita
```
The following converts every Markdown file from the `Downloads` directory to HTML and saves the HTML files to the `Destkop` directory.
```
MarkUP "/Users/user_name/Downloads" md_html -out "/Users/user_name/Desktop/"
```