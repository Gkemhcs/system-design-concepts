from user import User
from errors import UserNotFoundError
from reservation import Reservation
class UserManager:

    def __init__(self):
        self._users:dict[int,User]={}
        self._nextUserID:int=1
    def create_user(self,name:str,location:str)->User:
        user=User(self._nextUserID,name,location)
        self._users[self._nextUserID]=user
        self._nextUserID+=1
        print(f"creating user {user.get_user_id()}")
        return user 
    def delete_user(self,userID:int):
        if userID not in self._users :
            raise UserNotFoundError("the user you are trying to delete not exist")
        else:
            print(f"deleting the user {userID}")
            del self._users[userID]
            
    def add_reservation(self,reservation:Reservation):
        user=self._users.get(reservation._user.get_user_id(),None)
        if user is not None:
            user.add_reservation(reservation)
        else:
            raise UserNotFoundError("the user for this reservation not found")
    def remove_reservation(self,reservation:Reservation):
        user=self._users.get(reservation._user.get_user_id(),None)
        if user is not None:
            user.clear_reservation(reservation)
        else:
            raise UserNotFoundError("the user for this reservation not found")