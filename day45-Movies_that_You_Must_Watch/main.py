from bs4 import BeautifulSoup
import requests

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
response = requests.get(URL)

website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")
all_movies = soup.find_all("h3", class_="title")
with open('movies.txt', 'w') as data:
    for movie in reversed(all_movies):
        data.write(f"{movie.getText()}\n")