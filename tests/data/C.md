
# MarkUP

Batch-convert Markdown and HTML files. CHANGED

## Before you begin

1. Download the newest MarkUP version. See [Download MarkUP](https://github.com/rafalkaron/MarkUP/releases/latest).
2. Unzip **MarkUP**.

## Usage

1. In terminal, run: `markup <input> <conversion_type> -output_dir <output_dir>`
    Where:
    * **&lt;input&gt;** (required) is the file or directory that contains files that you want to convert.
    * **&lt;conversion_type&gt;** (required) is one of the following:
        * `md_dita` - converts Markdown to DITA
        * `html_dita` - converts HTML to DITA
        * `md_html` - Converts Markdown to HTML
        * `html_md` - Converts HTML to Markdown
    * **-output_dir** or **-out** (optional) precede the directory where you want to save the converted files.  
    **TIP:** By default the output directory is the same as the input directory.
2. If needed, accept any security prompt.

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
