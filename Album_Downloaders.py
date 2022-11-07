import urllib,os,time
import requests
from bs4 import BeautifulSoup
from requests import get

def getUrl(link):
    return link[link.index("https"):link.index("html")+4]

def download(url,movie_path):
    response = requests.get(url)
    soup = BeautifulSoup(response.content,"lxml")
    links = soup.find_all('a')
    for tag in links:
        link = tag.get('href',None)
        if link is not None and link.endswith("mp3"):
            file_name = tag.text
            print("     --> "+file_name + "  song is started.")
            with open(movie_path + "//"+file_name, "wb") as file:
                response = requests.get(link)
                file.write(response.content)
            print("     --> "+file_name + "  song is completed.")

def google_Search(search):
    response = requests.get("https://www.google.co.in/search?q="+search)
    soup = BeautifulSoup(response.content,"lxml")
    tags = soup.find_all('a')
    for tag in tags:
        link = tag.get('href',None)
        if link is not None and ("naasongs" in link):
            url = getUrl(link)
            return  url
    return None

def movie_search(movie_Name):
    search = movie_Name + "%20songs"
    movie_path = '/home/swaraj/songs/Audio/'+movie_Name
    if os.path.isdir(movie_path):
        print(movie_Name + " Album already Exists !!!")
        return None
    else:
        os.mkdir(movie_path)
    url = google_Search(search)
    if url is not None:
        download(url,movie_path)
        print(movie_Name+" Album downloaded.")
    else:
        print(" Download failed !!!")
if __name__ == "__main__":
    movie_Names = ['Bahubali']
    for movie in movie_Names:
        movie_search(movie)
