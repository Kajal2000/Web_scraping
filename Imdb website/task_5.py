from imdb_task_1 import*
from task_4 import*

def get_movie_list_details(url_list):
    movie_data_10 = []
    for i in url_list[:10]:
        url_1 = i["movie_link"]
        data = scrape_movie_details(url_1)
        movie_data_10.append(data)
    return (movie_data_10)
get_movie_details= get_movie_list_details(all_data)
# pprint.pprint(get_movie_details)