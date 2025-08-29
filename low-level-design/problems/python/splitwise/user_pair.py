from user import User
class UserPair:

    def __init__(self,user1:User,user2:User):
        self.__user1:User=user1 
        self.__user2:User=user2 
    
    def get_user1(self)->User:
        return self.__user1
    def get_user2(self)->User:
        return self.__user2
    
    def __str__(self)->str:
        return f"{self.__user1.get_name()}---->{self.__user2.get_name()}"
    