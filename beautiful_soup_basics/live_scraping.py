from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
y_combinator = response.text

soup = BeautifulSoup(y_combinator, "html.parser")

first_item = soup.find_all("span", class_="titleline")

first_refs = []


for i in first_item:
    text = i.getText()
    first_ref = i.get("ref")
    #first_text.append(text)
    first_refs.append(first_ref)

#print(first_text)
#print(first_refs)

all_points = soup.find_all("span", class_="score")
first_points = []

for i in all_points:
    point = i.getText()
    point = int(point.split()[0])
    first_points.append(point)

print(first_points)

max_number = 0

for number in first_points:
    if number > max_number:
        max_number = number

print(max_number)
