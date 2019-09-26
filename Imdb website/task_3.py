# from imdb_task import all_data as a
from task_2 import*

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
pprint.pprint(group_year_data)
