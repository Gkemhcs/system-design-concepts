from service.movie_service import MovieService
from core_classes.movie import Movie 


class MovieController:

    def __init__(self,movie_service:MovieService):
        self.__movie_service=movie_service

    def create_movie(self,name:str,duration:int)->Movie:
        return self.__movie_service.create_movie(name,duration)

    def get_movie(self,id:int)->Movie:
        return self.__movie_service.get_movie(id)
