from task_4 import*
from imdb_task_1 import*
from task_12 import*

def scrape_all_movie_cast(movie_caste_url):
    movie_data_10 = []
    for i in movie_caste_url[:250]:
        url_1 = i["movie_link"]
        data = scrape_movie_details(url_1)
        movie_cast1 = scrape_movie_cast(url_1)
        data["cast_name"] = movie_cast1
        movie_data_10.append(data)
    return (movie_data_10)
all_movie_cast_data = scrape_all_movie_cast(all_data)
# pprint.pprint(all_movie_cast_data)
