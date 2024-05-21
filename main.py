from bs4 import BeautifulSoup
import requests
response=requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
website_html=response.text
soup=BeautifulSoup(website_html,"html.parser")
all_movies=soup.find_all(name="h3",class_="title")
movies_title=[movies.getText() for movies in all_movies]
movies=movies_title[::-1]
with open("movies.txt",mode="w",encoding="utf8") as file:
    for movie in movies:
        file.write(f"{movie}\n")