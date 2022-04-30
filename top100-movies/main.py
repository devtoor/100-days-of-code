from __future__ import annotations

import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

content = requests.get(URL).text
soup = BeautifulSoup(content, "html.parser")

titles = [item.getText() for item in soup.find_all(name="h3", class_="title")][::-1]

with open("movies.txt", "w") as file:
    for title in titles:
        file.write(f"{title}\n")
