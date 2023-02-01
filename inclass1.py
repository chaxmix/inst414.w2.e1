import json

counter = 0

with open("imdb_movies_1985to2022.json","r") as in_file:
    for line in in_file:
        print(line)
        this_movie = json.loads(line)
        
        actors = this_movie["actors"]
        for actor in actors:
            actor_name = actor[1]
            print("\t", actor_name)
        
        counter += 1
        if counter > 5:
            break 
  

