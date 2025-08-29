class User:

    def __init__(self,id:int,name:str,email:str):
        self.__id=id 
        self.__name=name 
        self.__email=email 

    def get_id(self)->int:
        return self.__id 
    def get_name(self)->str:
        return self.__name 
    
    def get_email(self)->str:
        return self.__email 