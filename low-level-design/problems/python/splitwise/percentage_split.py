from split import Split 
from user import User 


class PercentageSplit(Split):

    def __init__(self):
        pass 

    def split(self,participants:list[User],amount:float,split_details:dict[User,any])->dict[User,float]:

            user_shares:dict[User,float]={}
            for user in participants:
                percent=split_details.get(user,0)
                user_shares[user]=round((percent*amount)/100,2)
            return user_shares 
