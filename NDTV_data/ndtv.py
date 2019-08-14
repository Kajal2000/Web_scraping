import requests
import pprint
from bs4 import BeautifulSoup

def scrape_ndtv_data():
    url = "https://www.ndtv.com/india?pfrom=home-mainnavgation"
    get_url = requests.get(url)
    main_data = BeautifulSoup(get_url.text,"html.parser")
    main_div = main_data.find("div", class_="ins_lftcont640 clr")
    div = main_div.find("div",class_="ins_left_rhs")
    ul_data = div.find("ul")
    li_data = ul_data.findAll("li")
    all_data_list = []
    for i in li_data:
        all_data_dic = {}
        try:
                data_link = i.find("div",class_="nstory_header")
                a_data = i.find("a")
                data_link = a_data["href"]
                # print(data_link)
        except TypeError:
                continue
        get_link = requests.get(data_link)
        main_link = BeautifulSoup(get_link.text,"html.parser")
        # print (main_link)
        main_div1 = main_link.find("div",class_="ins_dateline").get_text()
        pip_data = main_div1.split("|")
        # print (pip_data)
        edited_by = pip_data[1]
        # print (edited_by)
        date_time = pip_data[2]
        # print (date_time)
        m_div = main_link.find("div",class_="ins_lftcont640 clr")
        # print (m_div)
        head_line = m_div.find("div",class_="ins_headline").span.get_text()
        # print (head_line)
        p_graph = main_link.find("div",class_="ins_storybody").p.get_text()
        # print (p_graph)
        all_data_dic["edited_by"]=edited_by
        all_data_dic["date_time"]=date_time
        all_data_dic["head_line"]=head_line
        all_data_dic["p_graph"]=p_graph
        all_data_dic["data_link"]=data_link
        all_data_list.append(all_data_dic)
    return (all_data_list)
ndtv_data = scrape_ndtv_data()
pprint.pprint(ndtv_data)
