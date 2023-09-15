from bs4 import BeautifulSoup
import lxml

#               SCRAPING website.html

with open("website.html", encoding="utf-8") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")

#print(soup.prettify())
#print(soup.h3.string)

get_attributes = soup.findAll(name="a")
#print(headings)

#for i in headings:
  #  print(i.get("href"))

headings = soup.find(name="h3", class_="heading")
#print(headings.get_text())

get_lists = soup.findAll(name="li")

for i in get_lists:
  #  print(i.get_text())
    pass

#print(get_lists)

get_app_brewery = soup.select_one(selector="p a")
#print(get_app_brewery)

get_hobbies = soup.select("a")
print(get_hobbies)

