from imdb_task_1 import*
from task_4 import*
import os.path
import json

def chaching_movie_details(url_list):
    for i in url_list[:250]:
        url_1 = i["movie_link"]
        movie_id = url_1.split("/")
        get_id = movie_id[5]
        file_name = "data_c/"+get_id+".json"
        if os.path.exists(file_name): 
            with open(file_name,"r") as file:
                readFile=file.read()
                dictData=json.loads(readFile)
            return (dictData)
        else:
            data = scrape_movie_details(url_1)
            # print (data)
            print ("__________________________")
            with open(file_name,"w") as writeFile:
                stringData =json.dumps(data)
                writeFile.write(stringData)
    return (data)
movie_details_chaching = chaching_movie_details(all_data)
pprint.pprint(movie_details_chaching)