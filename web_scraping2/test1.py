import pdfplumber
import os
import json

file = r"/web_scraping2\corona.pdf"

if not os.path.exists(file):
    print(f"The file {file} does not exist.")
    exit(1)

folder_name = "web_scraping2"

if not os.path.exists(folder_name):
    os.makedirs(folder_name)

with pdfplumber.open(file) as pdf:
    for i, page in enumerate(pdf.pages, start=1):
        table = page.extract_table()
        if table:
            with open(os.path.join(folder_name, f"table_{i}.json"), 'w') as f:
                json.dump(table, f, indent=2)

print("Extraction complete.")
