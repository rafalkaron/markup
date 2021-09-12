
# MarkUP

Batch-convert Markdown and HTML files.

## Before you begin

1. Download the newest MarkUP version. See [Download MarkUP](https://github.com/rafalkaron/MarkUP/releases/latest).
1. Unzip **MarkUP**.

## Usage

<li>In terminal, run: `markup <input> <conversion_type> -output_dir <output_dir>` 
 Where:<ul>
1. **<input>** (required) is the file or directory that contains files that you want to convert.
<li>**<conversion_type>** (required) is one of the following:<ul>
1. `md_dita` - converts Markdown to DITA
1. `html_dita` - converts HTML to DITA
1. `md_html` - Converts Markdown to HTML
1. `html_md` - Converts HTML to Markdown
</ul>
</li>
<li>**-output_dir** or **-out** (optional) precede the directory where you want to save the converted files.<br>
**TIP:** By default the output directory is the same as the input directory.</li>
</ul>
</li>
1. If needed, accept any security prompt.

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
