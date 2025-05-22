class MovieCatalog:

    #catalog: dict[str, list[str]] = dict() ATTRIBUTO DI CLASSE
    #catalog: dict[str, list[str]] ATTRIBUTO DI ISTANZA

    def __init__(self):

        self.catalog: dict[str, list[str]] = {} 
        

    def add_movie(self, director_name:str, movies:list[str]):

        if director_name not in self.catalog:

            self.catalog[director_name] = movies 

        else:

            for movie in movies:
                
                if movie not in self.catalog[director_name]:

                    self.catalog[director_name].append(movie)

                else:

                    print("Il film già è presente")

                

    
    
    def remove_movie(self, director_name:str, movie_name:str):

        if director_name in self.catalog and movie_name in self.catalog[director_name]:

            self.catalog[director_name].remove(movie_name)

            if not self.catalog[director_name]:

                del self.catalog[director_name]

        else: 

            print("Non è presente nessun direttore o film che stai cercando di eliminare")

    
    
    def list_directors(self) ->list[str]:
        
        return list(self.catalog.keys())

    
    
    def get_movies_by_director(self,director_name:str) -> list[str]:
        
        if director_name in self.catalog:

            return self.catalog[director_name]
        
        else:

            print("Error")

    
    
    def search_movies_by_title(self, title:str) ->dict[str,list[str]] | str :

        result:dict[str, list[str]] = {}

        for director,movies in self.catalog.items():

            matching_movies: list[str] = []


            for movie in movies:

                if title.lower() in movie.lower():

                    matching_movies.append(movie)

            if matching_movies:

                result[director] = matching_movies

            else:

                return "Error"

        if result:

            return result
        
        else:

            return "Non è stato trovato nulla"



    