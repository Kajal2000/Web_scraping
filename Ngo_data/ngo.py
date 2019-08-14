import requests
import pprint
from bs4 import BeautifulSoup

def list_indian_ngo():
    all_data_list = []
    main_url = "https://www.giveindia.org/certified-indian-ngos"
    url_data = requests.get(main_url)
    main_data = BeautifulSoup(url_data.text,"html.parser")
    # print (main_data)
    table1 = main_data.find("table",class_="jsx-697282504 certified-ngo-table")
    # trs = table1.findAll("tr")

    trs = table1.findAll("tr",class_="jsx-697282504")
    for i in trs:
        # print(i)
        all_data_dic = {}
        name = i.find("div",class_='col')
        if name is not None:
            ngo_name = name.get_text()
            # print(ngo_name)
        try:
            td_list = i.find_all("td")[1]
        except IndexError:
            # print ("shi h")
            continue
        cause = ''.join(td_list.contents)
        # print (cause)

        try:
            td_list = i.find_all("td")[2]
        except IndexError:
            print ("shi h")
            continue
        state = ''.join(td_list.contents)
        # print (state)
        all_data_dic["ngo_name"]=ngo_name
        all_data_dic["cause"]=cause
        all_data_dic["state"]=state
        
        all_data_list.append(all_data_dic)
    return (all_data_list)
all_data = list_indian_ngo()
pprint.pprint(all_data)