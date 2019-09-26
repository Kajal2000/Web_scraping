from task_5 import*
from task_7 import*
all_dictionary = {}
def analyse_language_and_directors(movies_list):
   language_list = []
   duplicated_list = []
   for i in directors_list_data:
      for j in movies_list:
         if i in j["dictor_list"]:
            language_list.extend(j["movie_language"])
      for k in language_list:
         if k not in duplicated_list:
            duplicated_list.append(k)
      for x in duplicated_list:
         count = 0
         dictionary = {}
         for y in language_list:
            if y == x:
               count = count + 1
         dictionary[x] = count
      all_dictionary[i] = dictionary
   return (all_dictionary)
analyse_language = analyse_language_and_directors(get_movie_details)
# pprint.pprint(analyse_language)




