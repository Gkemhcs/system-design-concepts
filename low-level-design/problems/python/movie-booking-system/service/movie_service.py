from core_classes.movie import Movie 


class MovieService:

    def __init__(self):
        self.__movies:dict[int:Movie]={}
        self.__movie_counter=1
    
    def create_movie(self,name:str,duration:int)->Movie:

        id=self.__movie_counter
        movie=Movie(id,name,duration)
        self.__movies[id]=movie 
        print(f"movie of name {name} got created")
        self.__movie_counter+=1
        return movie 
    def get_movie(self,id:int)->Movie:

        if id not in self.__movies:
            raise Exception("sorry the movie doesnt exist")
        else:
            return self.__movies[id]
    




