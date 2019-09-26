from task_13 import*


def analyse_actors(movies_list):
    actors = {}
    for i in movies_list:
        # pprint.pprint (i)
        all_cast1 = i["cast_name"]

        for j in all_cast1:
            cast_name1 = j["name"]
            cast_id = j["imdb_id"]
            # print (cast_id)
            for cast in all_cast1:
                if cast_id == cast["imdb_id"]:
                    if cast_id not in actors:
                        actors[cast_id] = {}
                        # print (actors)
    #                     actors[cast_id]["name"] = cast_name1
    #                     actors[cast_id]["num"] = 1
    #                 else:
    #                     actors[cast_id]["num"] =  actors[cast_id]["num"] + 1
    # return (actors)
analyse_actors_data = analyse_actors(all_movie_cast_data)
# pprint.pprint(analyse_actors_data)