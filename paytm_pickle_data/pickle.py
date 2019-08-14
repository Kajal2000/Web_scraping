import requests
from bs4 import BeautifulSoup
import pprint
def scrap_pickle_data():
    all_data_list = []
    url = "https://paytmmall.com/fmcg-sauces-pickles-glpid-101471?page=1&latitude=12.868065800000002&longitude=77.7128736"
    get_url = requests.get(url)
    main_url = BeautifulSoup(get_url.text,"html.parser")
    main_div = main_url.findAll("div",class_="_2i1r")
    for i in main_div:
        all_data_dic = {}
        # print(i)
        name = i.find("div", class_="_2apC").get_text()
        # print (name)
        prise = i.find("div", class_="_1kMS").get_text()
        link = i.find("div", class_="_3WhJ").a["href"]
        url_link = "https://paytmmall.com"+link
        # print (url_link)
        poster = i.find("div",class_="_3nWP")
        # print (poster) 
        all_data_dic["name"]=name
        all_data_dic["prise"]=prise
        all_data_dic["url_link"]=url_link
        all_data_dic["poster"]=poster
        all_data_list.append(all_data_dic)
    return (all_data_list)
data = scrap_pickle_data()
pprint.pprint(data)
# scrap_pickle_data()