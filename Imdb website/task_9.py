from imdb_task_1 import*
from task_4 import*
import os.path
import json
import random
import time

def sleep_movie_list_details(url_list):
    # for i in url_list[:10]:
    random_data1 = random.randint(1,3)
    for i in url_list[:250]:
        url_1 = i["movie_link"]
        movie_id = url_1.split("/")
        get_id = movie_id[5]
        file_name = "chaching/"+get_id+".json"
        if os.path.exists(file_name): 
            with open(file_name,"r") as file:
                readFile=file.read()
                dictData=json.loads(readFile)
                # print (dictData)
        else:
            data = scrape_movie_details(url_1)
            print (data)
            print ("__________________________")
            with open(file_name,"w") as writeFile:
                stringData =json.dumps(data)
                writeFile.write(stringData)
                time.sleep(random_data1)
get_movie_rendom_details = sleep_movie_list_details(all_data)
pprint.pprint(get_movie_rendom_details)