from split import Split
from user import User

class EqualSplit(Split):

    def __init__(self):
        pass 
    def split(self,participants:list[User],amount:float,split_details:dict[User,any])->dict[User,float]:
        total_participants=len(participants)

        per_person_share:float=round(amount/total_participants,2)
        user_shares:dict[User,float]={}
        for  user in participants:
            
            user_shares[user]=per_person_share
        return user_shares