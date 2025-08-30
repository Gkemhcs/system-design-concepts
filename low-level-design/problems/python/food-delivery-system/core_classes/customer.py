from .user import User 
from .location import Location

class Customer(User):

    def __init__(self,id:int,name:str,email:str,phone_number:int,location:Location):
        super().__init__(id,name,email,phone_number,location)
    