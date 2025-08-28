

class User:

    def __init__(self,id:int,name:str,email:str):
        self._id=id 
        self.__name=name 
        self.__email=email 

    def get_id(self)->int:
        return self._id 
    def get_name(self):
        return self.__name 
    def get_email(self):
        return self.__email 