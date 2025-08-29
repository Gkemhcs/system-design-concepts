from abc import ABC,abstractmethod
from user import User 

class Split(ABC):

    @abstractmethod
    def split(participants:list[User],amount:float,split_details:dict[User,any])->dict[User,float]:
        pass 
