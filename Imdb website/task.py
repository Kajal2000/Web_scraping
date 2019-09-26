import requests
import pprint
from bs4 import BeautifulSoup 

def scrape_top_list():
    all_data_list = []
    url = "https://www.imdb.com/india/top-rated-indian-movies/"
    # print (url)
    get_url = requests.get(url)
    main_data = BeautifulSoup(get_url.text,"html.parser")
    t_body = main_data.find("tbody",class_="lister-list")
    # print(t_body)
    trs = t_body.findAll("tr")
    j = 0
    for i in trs:
        all_data_dic = {}
        position = j = j + 1
        name = i.find("td",class_="titleColumn").a.get_text()
        # print (name)
        year = i.find("td",class_="titleColumn").span.get_text()
        # print (year)
        rating = i.find("td",class_="ratingColumn imdbRating").get_text()
        # print (rating)
        movie_url = i.find("a")
        movie_link = "https://www.imdb.com/"+movie_url["href"]
        # print (movie_link)
        all_data_dic["name"]=name
        all_data_dic["year"]=int(year[1:5])
        all_data_dic["rating"]=float(rating)
        all_data_dic["movie_link"]=movie_link
        all_data_dic["position"]=position
        all_data_list.append(get_movie_list_detailsall_data_dic)
    return(all_data_list)
all_data = scrape_top_list()
# pprint.pprint (all_data)

# 2 ################################################################

def group_by_year(movies):
    group_year = [] 
    year_dic = {}
    for i in movies:
        # print (i)
        years = i["year"]
        if years not in group_year:
            group_year.append(years)
    for i in group_year:
        year_dic[i] = []
        # print (year_dic)
    for j in movies:
        year_list = j["year"]
        for i in year_dic:
            if i == year_list:
                 year_dic[i].append(j)
    return (year_dic)
year_data = group_by_year(all_data)  
# pprint.pprint (year_data)

# # 3 #############################################################################
def group_by_decade(movies):
    year_list = []
    year_dic = {}
    for i in movies:
        # print (i)
        year_mod = i%10
        # print (year_m)
        year_min = i-year_mod
        # print (year_min)
        if year_min not in year_list:
            year_list.append(year_min)
        # print (year_list)
        year_list.sort()
        # print (year_list)
    for i in  year_list:
        year_dic[i] = []
    for i in year_dic:
        # print (i)
        decade_10 = i+9
        # print (decade_10)
        for j in movies:
            # print (j)
            if j <= decade_10 and j >= i:
                for x in movies[j]:
                    year_dic[i].append(x)
    return (year_dic)
group_year_data = group_by_decade(year_data)
# pprint.pprint(group_year_data)

# # # 4 ########################################################################

def scrape_movie_details(movies):
    dictor_list = []
    url_list = []
    # for i in movies:
        # url_list.append(i['movie_link'])
    # data_1 = url_list[2]
    data_1_url = movies
    get_link = requests.get(data_1_url)
    # print (get_link)
    link_data = BeautifulSoup(get_link.text,"html.parser")
    bio = link_data.find("div",class_="summary_text").get_text().strip()
    poster_img = link_data.find("div", class_= "poster").a["href"]
    movie_poster = "https://www.imdb.com" + poster_img
    # print(movie_poster)
    runtime = link_data.find("time").get_text().strip()
    # print (runtime)
    runtime = link_data.find("div",class_="subtext")
    datetime1 = runtime.find("time")["datetime"]
    runtime1 = " "
    # print (type(datetime1))
    for i in datetime1:
        if i.isdigit():
            runtime1 = runtime1 + i
    # print (runtime1)     
    div_director = link_data.find("div",class_="credit_summary_item").a.get_text()
    dictor_list.append(div_director)
    m_genre = link_data.findAll("div",class_="subtext")
    name = link_data.find("div",class_="title_bar_wrapper").h1.get_text()
    m_name = name.split()
    movie_name = " ".join(m_name[:-1])
    # print (movie_name)
    genre_list = []
    for i in m_genre:
        genre = i("a")
        genre1 = genre[0:2]
        for i in genre1:
            movie_genre = (i.get_text())
            # print (movie_genre)
            genre_list.append(movie_genre) 
        # print (genre_list)
    m_country = link_data.find("div", class_="article",id="titleDetails")
    country = m_country.find("div", class_="txt-block").a.get_text()
    # print (country)
    m_lan = m_country.findAll("div")
    Language_list=[]
    for i in m_lan:
        tag_h4 = i.findAll("h4")
        # print (tag_h4)
        for j in tag_h4:
            if "Language:" in j:
                tag_a = i.findAll("a")
                # print (tag_a)
                for Language in tag_a:
                    movie_language = Language.get_text()
                    # print (movie_language)
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
    return (movie_details_dic)
movie_details = scrape_movie_details(all_data)
# pprint.pprint(movie_details)

# ##  5 ##################################################################

# def get_movie_list_details(url_list):
#     movie_data_10 = []
#     # for i in url_list[:20]:
#     for i in url_list[:10]:
#         # print (i)
#         url_1 = i["movie_link"]
#         # print (url_1)
#         data = scrape_movie_details(url_1)
#         # print (data)
#         movie_data_10.append(data)
#     return (movie_data_10)
# get_movie_details= get_movie_list_details(all_data)
# # pprint.pprint(get_movie_details)

# ## 6 ##############################################
def all_movies_languages(movies_list):
    Language_list_data = []
    for i in movies_list:
        get_Language = i["movie_language"]
        Language_list_data.extend(get_Language)
    return(Language_list_data)
# function calling
all_languages=all_movies_languages(get_movie_details)

Language_list_data1 = []
def languages(language):
    for j in language:
        if j not in Language_list_data1:
            Language_list_data1.append(j)
    return(Language_list_data1)
# function calling
particular_languages=languages(all_languages)

def analyse_movies_language(all_languages,particular_languages):  
    dictionary={}
    for x in particular_languages:
        count = 0
        for y in all_languages:
            if x == y:
                count = count + 1
        dictionary[x]=count
    return (dictionary)
# function calling
counting_of_language = analyse_movies_language(all_languages,particular_languages)
# pprint.pprint(counting_of_language)

# ## 7 ########################################################################
# def analyse_movies_directors(movies_list):
#     directors_list = []
#     for i in movies_list:
#         get_directors = i["dictor_list"]
#         directors_list.extend(get_directors)
#     return(directors_list)
# all_directors_data = analyse_movies_directors(get_movie_details)
# # pprint.pprint(all_directors_data)

# directors_list_data = []
# def directors(director):
#     for j in director:
#         if j not in directors_list_data:
#             directors_list_data.append(j)
#             # print (directors_list_data)
#     return(directors_list_data)
# particular_directors = directors(all_directors_data)
# # pprint.pprint(particular_directors)

# def analyse_movies_directors1(particular_directors,all_directors_data):  
#     dictionary1={}
#     for x in particular_directors:
#         count1 = 0
#         for y in all_directors_data:
#             if x == y:
#                 count1 = count1 + 1
#         dictionary1[x]=count1
#     return (dictionary1)
# counting_of_directors = analyse_movies_directors1(particular_directors,all_directors_data)
# # pprint.pprint(counting_of_directors)


