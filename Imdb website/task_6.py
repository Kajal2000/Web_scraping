from task_5 import*

def all_movies_languages(movies_list):
    Language_list_data = []
    for i in movies_list:
        get_Language = i["movie_language"]
        Language_list_data.extend(get_Language)
    return(Language_list_data)
# function calling
all_languages=all_movies_languages(get_movie_details)

Language_list_data1 = []
def languages(language):
    for j in language:
        if j not in Language_list_data1:
            Language_list_data1.append(j)
    return(Language_list_data1)
# function calling
particular_languages=languages(all_languages)

def analyse_movies_language(all_languages,particular_languages):  
    dictionary={}
    for x in particular_languages:
        count = 0
        for y in all_languages:
            if x == y:
                count = count + 1
        dictionary[x]=count
    return (dictionary)
counting_of_language = analyse_movies_language(all_languages,particular_languages)
pprint.pprint(counting_of_language)