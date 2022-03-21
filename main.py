import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(url=URL)
text = response.text
soup = BeautifulSoup(text, "html.parser")

file = open("100_best_movies.txt", "w")
article_titles = [title.getText() for title in soup.find_all(name="h3", class_="title")]
article_titles = article_titles[::-1]
for title in article_titles:
    file.write(f"{title}\n")


