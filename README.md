
# MarkUP

Batch-convert Markdown and HTML files.

## Before you begin

1. Download the newest **MarkUP**. See [Download MarkUP](https://github.com/rafalkaron/MarkUP/releases/latest).
2. Unzip **MarkUP**.

## Convert documents

1. In terminal, enter `markup` followed by these parameters:
    | Parameter              | Required | Description                                           |
    |------------------------|----------|-------------------------------------------------------|
    | **`<input>`**          | Yes      | Path to a file or directory containing files to convert. |
    | **`<conversion_type>`** | Yes      | One of the following conversion modes: <ul><li>`md_dita` - Converts Markdown to DITA.</li><li>`html_dita` - Converts HTML to DITA.</li><li>`md_html` - Converts Markdown to HTML.</li><li>`html_md` - Converts HTML to Markdown.</li></ul> |
    | **`-out <output_dir>`** | No       | Directory for the converted files (defaults to the input directory). |

2. If needed, accept any security prompts.  
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
