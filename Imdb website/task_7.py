from task_5 import*

def analyse_movies_directors(movies_list):
    directors_list = []
    for i in movies_list:
        get_directors = i["dictor_list"]
        directors_list.extend(get_directors)
    # print (directors_list)
    return(directors_list)
all_directors_data = analyse_movies_directors(get_movie_details)
# pprint.pprint(all_directors_data)

directors_list_data = []
def directors(director):
    for j in director:
        if j not in directors_list_data:
            directors_list_data.append(j)
            # print (directors_list_data)
    return(directors_list_data)
particular_directors = directors(all_directors_data)
# pprint.pprint(particular_directors)

def analyse_movies_directors1(particular_directors,all_directors_data):  
    dictionary1={}
    for x in particular_directors:
        count1 = 0
        for y in all_directors_data:
            if x == y:
                count1 = count1 + 1
        dictionary1[x]=count1
    return (dictionary1)
counting_of_directors = analyse_movies_directors1(particular_directors,all_directors_data)
# pprint.pprint(counting_of_directors)


