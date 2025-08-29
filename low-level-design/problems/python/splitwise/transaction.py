from user import User 

class Transaction :

    def __init__(self,sender:User,receiver:User,amount:float):
        self.__sender=sender 
        self.__reciever=receiver    
        self.__amount=amount 
    
    def get_sender(self)->User:
        return self.__sender
    def get_receiver(self)->User:
        return self.__reciever
    def get_amount(self)->float:
        return self.__amount 