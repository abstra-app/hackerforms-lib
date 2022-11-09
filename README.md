[![pypi](https://img.shields.io/pypi/v/hackerforms.svg)](https://pypi.python.org/pypi/hackerforms)
[![PyPI Downloads](https://img.shields.io/pypi/dm/hackerforms.svg)](
https://pypi.org/project/hackerforms/)
[![Code check](https://github.com/abstra-app/hackerforms-lib/actions/workflows/code_check.yml/badge.svg)](https://github.com/abstra-app/hackerforms-lib/actions/workflows/code_check.yml)

# Hackerforms
Launch interactive Python scripts as beautiful form-like apps

![docs_editor](https://user-images.githubusercontent.com/8538337/200737655-7d212aef-e07a-4425-8cab-40000be3539d.gif)

No HTML, CSS, JS, BS... With single line commands, get data from users and display info to them

## Example
```Python
from hackerforms import *
import pandas as pd
from docxtpl import DocxTemplate
from datetime import datetime
import zipfile

Page().display("Hey there! Download the spreadsheet below and fill it with your customers' info.") \
    .display_file('files/customer_data_template.xlsx') \
    .run()

uploaded_file = read_file("Upload the completed spreadsheet below:")
file_content = uploaded_file.content

df = pd.read_excel(file_content)

selection = read_pandas_row_selection(df, hint = "Select which customers you'd like to generate an invoice to.")

doc = DocxTemplate('files/invoice_template.docx')

list = []

for item in selection:
    name = item['Name']
    item["Date"] = pd.to_datetime(item["Date"]).strftime("%Y-%m-%d")
    doc.render(item)
    file_name = f'/tmp/Template_rendered_{name}.docx'
    doc.save(file_name)
    list.append(file_name)

with zipfile.ZipFile('/tmp/invoices.zip', 'w') as zipF:
    for invoice in list:
        zipF.write(invoice, compress_type=zipfile.ZIP_DEFLATED)

Page().display(f"Your invoices are ready! Download them below:") \
    .display_file('invoices.zip') \
    .run()

display("See you next time!")
```

[See all widgets here](https://docs.abstracloud.com/library/widgets)

## Installation

```bash
pip install hackerforms
```
## Links

- [Examples](https://github.com/abstra-app/hackerforms-examples/tree/master/python)
- [Docs](https://docs.abstracloud.com/)



