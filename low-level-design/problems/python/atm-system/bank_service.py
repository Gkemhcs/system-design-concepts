from card import Card
from account import Account 
from card_type import CardType
from errors import AccountAlreadyExistsError,CardAlreadyExistsError,AccountNotExistsError,CardNotExistError
class BankService:

    def __init__(self):
        self._cards:dict[int,Card]={}
        self._card_account_map:dict[Card,Account]={}
        self._accounts:dict[int,Account]={}
    def create_account(self,account_number:int,account_name:int,balance:int=0.0)->Account:
        if account_number in self._accounts:
            raise AccountAlreadyExistsError("the account already exists try to create another account if you want")
        
        account=Account(account_number,account_name,balance)
        self._accounts[account_number]=account 
        return account
    def get_card(self,card_number)->Card:
     
        if card_number not in self._cards:
            raise CardNotExistError("sorry the card you have inserted is invalid")
        return self._cards[card_number]
    def get_account(self,account_number:int)->Account:
        if account_number not in self._accounts:
            raise AccountNotExistsError("sorry the account not exist")
        return self._accounts[account_number]
    def create_card(self,account_number:int,pin:int,card_number:int,card_type:CardType)->Card:
        if card_number in self._cards:
            raise CardAlreadyExistsError("sorry the card already exists")
        self.get_account(account_number)
        card=Card(account_number,pin,card_type,card_number)
        self._cards[card_number]=card 
        self._card_account_map[card]=self.get_account(account_number)
        return card 
    def check_balance(self,account_number:int)->float:
        if account_number not in self._accounts:
            raise AccountNotExistsError("sorry the account not exist")
        return self._accounts[account_number].get_balance()
    def deposit(self,account_number:int,amount:float)->float:
        if account_number not in self._accounts:
            raise AccountNotExistsError("sorry the account not exist")
        return self._accounts[account_number].deposit_amount(amount)
    def withdraw(self,account_number:int,amount:float)->float:
        if account_number not in self._accounts:
            raise AccountNotExistsError("sorry the account not exist")
        return self._accounts[account_number].withdraw(amount)
    def block_card(self,card_number:int):
        if card_number not in self._cards:
            raise CardNotExistError("sorry the card your are trying to block doesn't exist")
        else:
            card=self._cards[card_number]
            card.block_card()
    def unblock_card(self,card_number:int):
        if card_number not in self._cards:
            raise CardNotExistError("sorry the card your are trying to unblock doesn't exist")
        card=self._cards[card_number]
        card.unblock_card()
    def inactivate_account(self,account_number:int):
        if account_number  not in self._accounts:
            raise AccountNotExistsError("sorry the account you are trying to inactivate doesnt exist")
        account=self._accounts[account_number]
        account.inactivate_account()
    def activate_account(self,account_number:int):
        if account_number  not in self._accounts:
            raise AccountNotExistsError("sorry the account you are trying to activate doesnt exist")
        account=self._accounts[account_number]
        account.activate_account()
    def get_pin(self,card_number:int)->int:
         if card_number not in self._cards:
            raise CardNotExistError("sorry the card your are trying to get the pin doesnt exist")
         card=self._cards[card_number]
         return card.get_pin()
    def change_pin(self,card_number:int,new_pin:int):
        if card_number not in self._cards:
            raise CardNotExistError("sorry the card your are trying to change the pin doesnt exist")
        card=self._cards[card_number]
        card.change_pin(new_pin)
