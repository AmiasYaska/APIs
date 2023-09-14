from bs4 import BeautifulSoup
import lxml

with open("website.html", encoding="utf-8") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")

#print(soup.prettify())
#print(soup.h3.string)

headings = soup.findAll(name="a")
#print(headings)

for i in headings:
    print(i.get("href"))
