from task_13 import*
from pprint import pprint

def analyse_co_actors(movies_list):
    dict1={}
    for i in movies_list:
        # total_cast = i["cast_name"]
        actors1 = i["cast_name"][0]["name"]
        co_actor = i["cast_name"][1]["name"]
        actors2 = i["cast_name"][0]["imdb_id"]
        id1 = i["cast_name"][1]["imdb_id"]
        cast_dic = []
        for index in actors1:
            if actors1 not in cast_dic:
               cast_dic.append(actors1)

        for index1 in cast_dic:
            for cast in actors2:
                if actors2 not in dict1:
                    dict1[actors2] = {}
                    dict1[actors2]["ActorName"] = index1
                    dict1[actors2]["frequent_co_actors"] = []
                    analyse_co_dic = {} 
                    analyse_co_dic["num_movie"] = 1
                    analyse_co_dic["imdb_id"]= id1
                    analyse_co_dic["co_actor_name"] = co_actor
                    dict1[actors2]["frequent_co_actors"].append(analyse_co_dic)
                else:
                    number = 1
                    for i in dict1[actors2]["frequent_co_actors"]:
                        if i["imdb_id"] == total_cast[1]["imdb_id"]:
                            i["num_movie"] = i["num_movie"] + 1
                        number=number+1
                    if number == len(dict1[actors2]["frequent_co_actors"]):
                        analyse_co_dic = {} 
                        analyse_co_dic["imdb_id"] = total_cast[1]["imdb_id"]
                        analyse_co_dic["co_actor_name"] = total_cast[1]["name"]
                        dict1[actors2]["frequent_co_actors"].append(analyse_co_dic)            
    pprint(dict1)
analyse_co_actors(all_movie_cast_data)