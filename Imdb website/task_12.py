from imdb_task_1 import*
import os.path
import json

def scrape_movie_cast(movie_caste_url):
    url_list=[]
    # for i in movie_caste_url:
        # url_list.append(i['movie_link'])
    # link = url_list[0]
    link =  movie_caste_url      
    get_url = requests.get(link)
    soup = BeautifulSoup(get_url.text,"html.parser")
    main_div1=soup.find("div",class_="article",id="titleCast")
    main_div = main_div1.find("div",class_="see-more") 
    a_tag = main_div.find("a")["href"]
    total_cast_link = link+a_tag

    movie_id = total_cast_link.split("/")
    get_id = movie_id[5]

    file_name = "id_data_chaching/"+get_id+".json"
    if os.path.exists(file_name):
        with open(file_name,"r") as file:
            readFile=file.read()
            dictData = json.loads(readFile)
        return (dictData)
    else:
        get_url = total_cast_link
        get_link = requests.get(get_url)
        soup = BeautifulSoup(get_link.text,"html.parser")
        table_data = soup.find("table",class_="cast_list")
        trs = table_data.findAll("tr")
        all_cast = []
        for i in trs[1:]:
            try:
                tds = i.findAll("td")
                cast_link = tds[1].a["href"]
                cast_link1 = (cast_link).split("/")
                particur_cast = (cast_link1[2])
                cast_name = (tds[1].get_text())
            except IndexError:
                continue
            all_cast_dic = {}
            all_cast_dic["name"]=cast_name.strip("  \n")
            all_cast_dic["imdb_id"]=particur_cast
            all_cast.append(all_cast_dic)
        with open(file_name,"w") as file:
            dictData = json.dumps(all_cast)
            file.write(dictData)
    return (all_cast)
# all_cast_data = scrape_movie_cast(all_data)
# pprint.pprint(all_cast_data)
