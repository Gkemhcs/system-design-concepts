from user import User 
from split_types import SplitType
class Expense :

    def __init__(self,id:str,description:str,payer:User,amount:float,participants:list[User],user_shares:dict[User,float],split_type:SplitType=SplitType.EQUAL):

        self._id=id 
        self._description=description
        self.__payer:User=payer 
        self.__amount:float=amount 
        self.__split_type:SplitType=SplitType
        self.__participants:list[User]=participants 
        self.__user_shares:dict[User,float]=user_shares
        print(f"the expense of id {id} having description {description} got created")
    def get_id(self)->str:
        return self._id 
    def get_description(self)->str:
        return self._description
    def get_payer(self)->User:
        return self.__payer 
    def get_split_type(self)->SplitType:
        return self.__split_type
    def get_amount(self)->float:
        return self.__amount 

    def get_participants(self)->list[User]:
        return self.__participants
    def get_user_shares(self)->dict[User,float]:
        return self.__user_shares
    