from task_5 import*

def analyse_movies_genre(movies_list):
        genre_data = []
        for i in movies_list:
                get_genre = i["genre_list"]
                genre_data.extend(get_genre)
        return (genre_data)
all_genre_data = analyse_movies_genre(get_movie_details)

genre_data1 = []
def getGenre(genre1):
        for i in genre1:
                if i not in genre_data1:
                        genre_data1.append(i)
        return (genre_data1)
particular_genre = getGenre(all_genre_data)

def analyse_genre(all_genre_data,particular_genre):
        genre_dic = {}
        for a in particular_genre:
                count = 0
                for b in all_genre_data:
                        if a == b:
                                count = count + 1
                genre_dic[a] = count
        return(genre_dic)
count_genre = analyse_genre(all_genre_data,particular_genre)
# pprint.pprint(count_genre)