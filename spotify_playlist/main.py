from bs4 import BeautifulSoup
import requests

URL = "https://www.billboard.com/charts/hot-100/"
response = requests.get(URL)
billboard_songs = response.text

soup = BeautifulSoup(billboard_songs, "html.parser")

#user_year = input("Which year do you want to travel to? Type the date in this format"
 #                 "YYYY-MM-DD: ")

top_songs = soup.findAll("h3", id="title-of-a-story")

song_list = []

for song in top_songs:
    songs = song.getText()
    song_list.append(songs)

song_items = "\n".join(song_list)
print(song_items)
