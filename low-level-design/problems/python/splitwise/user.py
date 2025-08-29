

class User:
    def __init__(self,id:str,name:str,email:str,phone_number:int):

        self.__id=id 
        self._name=name 
        self.__email=email 
        self.__phone_number=phone_number
        print(f"user {name} with id {id} was created successfully")
    def get_id(self)->str:
        return self.__id 
    def get_name(self)->str:
        return self._name
    def get_email(self)->str:
        return self.__email 
    def get_phone_number(self)->int:
        return self.__phone_number
     
