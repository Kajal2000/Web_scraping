import requests
import pprint
from bs4 import BeautifulSoup 

def scrape_top_list():
    all_data_list = []
    url = "https://www.imdb.com/india/top-rated-indian-movies/"
    get_url = requests.get(url)
    main_data = BeautifulSoup(get_url.text,"html.parser")
    t_body = main_data.find("tbody",class_="lister-list")
    trs = t_body.findAll("tr")
    j = 0
    for i in trs:
        all_data_dic = {}
        position = j = j + 1
        name = i.find("td",class_="titleColumn").a.get_text()
        year = i.find("td",class_="titleColumn").span.get_text()
        rating = i.find("td",class_="ratingColumn imdbRating").get_text()
        movie_url = i.find("a")
        movie_link = "https://www.imdb.com/"+movie_url["href"]
        all_data_dic["name"]=name
        all_data_dic["year"]=int(year[1:5])
        all_data_dic["rating"]=float(rating)
        all_data_dic["movie_link"]=movie_link
        all_data_dic["position"]=position
        all_data_list.append(all_data_dic)
    return(all_data_list)
all_data = scrape_top_list()
# pprint.pprint (all_data)