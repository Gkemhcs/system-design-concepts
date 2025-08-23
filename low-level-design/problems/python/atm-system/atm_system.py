from bank_service import BankService
from cash_inventory import CashInventory
from transaction_manager import TransactionManager
from card_type import CardType
from denominations import Denomination
from account import Account
from card import Card
from transaction_types  import TransactionType
from idle_state import IdleState
from machine_states import MachineState
from observer import Observer
from errors import PINMisMatchError,MismatchedTransactionError,InsufficientAmountInATMError
class ATMSystem:

    def __init__(self):
        self._bank_service=BankService()
        self._cash_inventory=CashInventory()
        self._transaction_manager=TransactionManager()
        self._current_card:Card=None
        self._selected_operation:TransactionType=None
        self._current_state:MachineState=IdleState()
        self._max_attempts=3 
        self._attempts=0
    def create_account(self,account_number:int,account_name:int,balance:float=0.0)->Account:
        account=self._bank_service.create_account(account_number,account_name,balance)
        print(f"account successfully created for {account_name}")
        return account 
    def create_card(self,card_number:int,card_type:CardType,pin:int,account_number:int)->Card:
        card=self._bank_service.create_card(account_number,pin,card_number,card_type)
        print(f"card successfully created for account {account_number}")
        return card
    def change_pin(self,card_number:int):
    
        self._bank_service.change_pin(card_number)
        print(f"successfully changed pin for card {card_number}")
    def activate_account(self,account_number:int):
        self._bank_service.activate_account(account_number)
        print(f"successfully activated account {account_number}")
    def inactivate_account(self,account_number:int):
        self._bank_service.inactivate_account(account_number)
        print(f"successfully inactivated account {account_number}")
    def block_card(self,card_number:int):
        self._bank_service.block_card(card_number)
        print(f"successfully blocked card {card_number}")   
    def unblock_card(self,card_number:int):
        self._bank_service.unblock_card(card_number)
        print(f"successfully unblocked card {card_number}")

    def register_observer(self,observer:Observer):
        self._transaction_manager.register_observer(observer)
    def unregister_observer(self,observer:Observer):
        self._transaction_manager.unregister_observer(observer)
    def add_amount(self,cash_type:Denomination,count:int):
        print("successfuly added amount to cash inventory")
  
        self._cash_inventory.add_cash(cash_type,count)
    def change_state(self,state:MachineState):
        self._current_state=state
    def get_current_state(self):
        return self._current_state
    def remove_card(self):
        self._current_card=None
    def insert_card(self,card:Card):
        
        self._bank_service.get_card(card.get_card_number())
        self._bank_service.get_account(card.get_account_number())
        self._current_card=card 
        print(f"card numbered {card.get_card_number()}  has been successfully inserted")
        self._current_state.insert_card(self)
    def authenticate_card(self,pin:int):
        card_number=self._current_card.get_card_number()
      
        card=self._bank_service.get_card(card_number)
        
        if card.get_pin()!=pin:
            self._attempts+=1
            if self._attempts>self._max_attempts:
                self._attempts=0
                self._current_state.change_to_idle()
            raise PINMisMatchError("sorry the pin is not correct enter once again")
           
        else:
            print("ok you are authenticated now")
            self._current_state.authenticate_user(self)
    def display_available_transactions(self):
        print("\n----Available Methods----\n")
        i=1
        for val in TransactionType._value2member_map_:
            print(f"{i}:{val}")
            i+=1
        
    def select_transaction_type(self, transaction_type: TransactionType):
        self._selected_operation = transaction_type
        print()
        print(f"successfully selected transaction type {transaction_type.value}")
        self._current_state.dispense_cash(self)
        
    
    def check_balance(self)->float:
            
        if self._selected_operation!=TransactionType.CHECK_BALANCE:
            raise MismatchedTransactionError("sorry you havent selected balance as transaction type")
        account=self._bank_service.get_account(self._current_card.get_account_number())
        self._transaction_manager.record_transaction(TransactionType.CHECK_BALANCE,self._current_card.get_card_number(),account.get_account_number(),0)
        print("balance enquiry successful")
        self._current_state.change_to_idle(self)
        
        return account.get_balance()

    def withdraw(self,amount:float)->dict[Denomination,int]:
        if self._selected_operation!=TransactionType.WITHDRAW:
            raise MismatchedTransactionError("sorry you havent chosen withdraw")
        if not self._cash_inventory.is_sufficient(amount):
            raise InsufficientAmountInATMError("sorry the atm doesnt have sufficient amount")
        account=self._bank_service.get_account(self._current_card.get_account_number())
        if account.get_balance()<amount:
            raise InsufficientAmountInATMError("sorry the account doesnt have sufficient amount")
        denominations=self._cash_inventory.dispense_cash(amount)
        account.withdraw_amount(amount)
        self._transaction_manager.record_transaction(TransactionType.WITHDRAW,self._current_card.get_card_number(),account.get_account_number(),amount)
        print(f"successfully withdrawn the amount of {amount} rupees from account {account.get_account_number()}")
        self._current_state.change_to_idle(self)
        return denominations
    def deposit(self,denominations:dict[Denomination,int]):
        if self._selected_operation!=TransactionType.DEPOSIT:
            raise MismatchedTransactionError("sorry you havent chosen deposit as transaction type")
        account_number=self._current_card.get_account_number()
        self._cash_inventory.deposit_cash(denominations)
        amount=0
        for denomination in denominations.keys():
            amount+=denomination.value*denominations[denomination]
       
        self._bank_service.deposit(account_number,amount)
        self._transaction_manager.record_transaction(TransactionType.DEPOSIT,self._current_card.get_card_number(),account_number,amount)
        print(f"depositing the amount of {amount}rupees into {account_number}")
        self._current_state.change_to_idle(self)