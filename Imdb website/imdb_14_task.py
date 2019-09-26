from task_13 import*
from pprint import pprint


def analyse_co_actors(movies_list):
    lead_ids = {}
    for i in movies_list:
        all_cast = i["cast_name"]
        lead_actors_id = all_cast[0]["imdb_id"]
        lead_names = all_cast[0]["name"] 
        for j in movies_list:
            actor_cast = j["cast_name"]
            if lead_actors_id == actor_cast[0]["imdb_id"]:
                if lead_actors_id not in lead_ids:
                    lead_ids[lead_actors_id] = {}
                    lead_ids[lead_actors_id]["Actor_name"] = lead_names
                    lead_ids[lead_actors_id]["frequent_co_actors"] = []
                    co_dic = {}
                    co_dic["num_movies"] = 1
                    co_dic["name"] = actor_cast[1]["name"]
                    co_dic["co_actor_id"] = actor_cast[1]["imdb_id"]
                    lead_ids[lead_actors_id]["frequent_co_actors"].append(co_dic)
                else: 
                    number = 1
                    for count in lead_ids[lead_actors_id]["frequent_co_actors"]:
                        if count["co_actor_id"] == actor_cast[1]["imdb_id"]:
                            count["num_movies"] = count["num_movies"] + 1                  
                        number = number + 1
                    if number == len(lead_ids[lead_actors_id]["frequent_co_actors"]):
                        co_dic = {}
                        co_dic["num_movies"] = 1
                        co_dic["name"] = actor_cast[1]["name"]
                        co_dic["co_actor_id"] = actor_cast[1]["imdb_id"]
                        lead_ids[lead_actors_id]["frequent_co_actors"].append(co_dic)
                        
    return(lead_ids)
a= analyse_co_actors(all_movie_cast_data)
pprint(a)