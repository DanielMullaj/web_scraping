from bs4 import BeautifulSoup
import re

with open("index2.html", "r") as f:
    doc = BeautifulSoup(f, "html.parser")

res = doc.find_all(text=re.compile("\$.*"), limit=1)
for tag in res:
    print(tag)


