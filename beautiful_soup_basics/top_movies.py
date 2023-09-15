from bs4 import BeautifulSoup
import requests
#               SCRAPING TOP 100 MOVIES AND PUT IT IN ALL_MOVIES.TXT
response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")
top_movies = response.text

soup = BeautifulSoup(top_movies, "html.parser")

movie_titles = soup.findAll("h3")

movie_list = []

for movie in movie_titles:
    movie_title = movie.getText()
    movie_list.append(movie_title)

movie_list.reverse()

file_path = "all_movies.txt"
with open(file_path, "w") as file:
    for item in movie_list:
        file.write(f"{item}\n")

