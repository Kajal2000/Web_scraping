from imdb_task_1 import*
# from task_12 import*

def scrape_movie_details(movies):
    url_list = []
    # for i in movies:
        # url_list.append(i['movie_link'])
    # data_1 = url_list[110]
    data_1_url = movies
    get_link = requests.get(data_1_url)
    link_data = BeautifulSoup(get_link.text,"html.parser")
    bio = link_data.find("div",class_="summary_text").get_text().strip()
    poster_img = link_data.find("div", class_= "poster").a["href"]
    movie_poster = "https://www.imdb.com" + poster_img
    runtime = link_data.find("time").get_text().strip()
    runtime = link_data.find("div",class_="subtext")
    datetime1 = runtime.find("time")["datetime"]
    runtime1 = " "
    # print (type(datetime1))
    for i in datetime1:
        if i.isdigit():
            runtime1 = runtime1 + i
    name = link_data.find("div",class_="title_bar_wrapper").h1.get_text()
    m_name = name.split()
    movie_name = " ".join(m_name[:-1])

    ## div_director = link_data.find("div",class_="credit_summary_item").a.get_text()
    div_director = link_data.find("div",class_="credit_summary_item")
    dictor_list = []
    dictor = div_director.findAll("a")
    for i in dictor:
        dictor_list.append(i.get_text())

    m_genre = link_data.find("div",class_="subtext")
    genre_list = []
    genre = m_genre.findAll("a")
    genre.pop()
    for i in genre:
        movie_genre = i.get_text()
        genre_list.append(movie_genre)
    m_country = link_data.find("div", class_="article",id="titleDetails")
    country = m_country.find("div", class_="txt-block").a.get_text()
    m_lan = m_country.findAll("div")
    Language_list=[]
    for i in m_lan:
        tag_h4 = i.findAll("h4")
        for j in tag_h4:
            if "Language:" in j:
                tag_a = i.findAll("a")
                for Language in tag_a:
                    movie_language = Language.get_text()
                    Language_list.append(movie_language)
                # print (Language_list)
        movie_details_dic = {}
        movie_details_dic["movie_name"]= movie_name
        movie_details_dic["dictor_list"]=dictor_list
        movie_details_dic["genre_list"]=genre_list
        movie_details_dic["runtime1"]=int(runtime1)
        movie_details_dic["bio"]=bio
        movie_details_dic["movie_poster"]=movie_poster
        movie_details_dic["country"]=country
        movie_details_dic["movie_language"]=Language_list
        # movie_details_dic["cast_name"]=all_cast_data
    return (movie_details_dic)
# movie_details = scrape_movie_details(all_data)
# pprint.pprint(movie_details)
