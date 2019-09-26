# from imdb_task_1 import all_data as all_data_1
from imdb_task_1 import*

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