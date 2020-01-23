# [Pdf-To-Image](https://github.com/starkblaze01/Pdf-To-Image)
[![PyPI version](https://badge.fury.io/py/pdftoimg.svg)](https://badge.fury.io/py/pdftoimg)


Simple Command Line tool to convert PDF to Image.

# How to Install
`pip install pdftoimg`

### You need to install poppler if you don't have already.
- For Windows you can install it from [here](https://anaconda.org/conda-forge/poppler/files).
- For MacOS you can install it from [here](http://macappstore.org/poppler/).

## How to use
- Open terminal.
- Run `pdftoimg -h` for help.

#### Example usage:
- `pdftoimg -i /Users/starkblaze01/Bova/file_name.pdf -o /Users/starkblaze01/output_folder`

Definitions:
- -i for input pdf_file path
- -o for output_folder path
- -f for image format(Default: jpeg)
- -d for dpi(Default: 200)
- -g for grayscale image(Default: False)
