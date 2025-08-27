class Entity:
    def __init__(self,start:int,end:int):
        self.__start=start
        self.__end=end

    def get_start(self)->int:
        return self.__start 

    def get_end(self)->int:
        return self.__end 
