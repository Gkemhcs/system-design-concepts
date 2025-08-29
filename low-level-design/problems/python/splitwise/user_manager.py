from user import User


class UserManager:

    def __init__(self):
        self.__users:dict[str:User]={}
    
    def create_user(self,user_id:str,user_name:str,email:str,phone_number:int)->User:
        if user_id in self.__users:
            raise Exception("sorry the user already exists")
        else:
            user=User(user_id,user_name,email,phone_number)
            self.__users[user_id]=User
            return user

    def get_user_by_id(self,user_id:str)->User:
        if user_id not in self.__users:
            raise Exception("the user not present")
        else:
            return self.__users[user_id]