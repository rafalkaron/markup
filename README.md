
# MarkUP

Batch-convert Markdown and HTML files.

## Before you begin

1. Download the newest **MarkUP**. See [Download MarkUP](https://github.com/rafalkaron/MarkUP/releases/latest).
2. Unzip **MarkUP**.

## Convert documents

1. In a terminal, enter `markup <input> <conversion_type> -out <output_dir>`,  
    where:
    * **&lt;input&gt;** (required) is a path to a file or a directory that contains files to convert.
    * **&lt;conversion_type&gt;** (required) is one of the following:
        * `md_dita` - converts Markdown to DITA.
        * `html_dita` - converts HTML to DITA.
        * `md_html` - converts Markdown to HTML.
        * `html_md` - converts HTML to Markdown.
    * **-out &lt;output_dir&gt;** (optional) precedes the directory for the converted files.  
    **TIP:** By default, the output directory is the same as the input directory.
2. If needed, accept any security prompt.  
For more information, see [Accepting macOS Security Prompts](https://github.com/rafalkaron/MarkUP/wiki/Accepting-macOS-Security-Prompts) or [Accepting Windows Security Prompts](https://github.com/rafalkaron/MarkUP/wiki/Accepting-Windows-Security-Prompts).

## Examples

The following converts every Markdown file to DITA in the `Downloads` directory.

```zsh
markup "/Users/user_name/Downloads" md_dita
```

The following coverts the `README.html` file to DITA.

```zsh
markup "/Users/user_name/Desktop/README.html" html_dita
```

The following converts every Markdown file from the `Downloads` directory to HTML and saves the HTML files to the `Destkop` directory.

```zsh
markup "/Users/user_name/Downloads" md_html -out "/Users/user_name/Desktop/"
```
