from errors import AccountIsActiveError,AccountIsInactiveError,InsufficientBalanceInAccountError
class Account:

    def __init__(self,account_number:int,account_name:str,balance:float):
        self._account_number:int=account_number
        self._balance:float=balance
        self._is_active:bool=True
        self.account_name:str=account_name
    
    def get_account_number(self)->int:
        return self._account_number

    def get_account_name(self)->str:
        return self._account_name

    def inactivate_account(self):
        if not self._is_active:
            raise AccountIsInactiveError("account is already inactive")
        self.is_active = False
    def activate_account(self):
        if self._is_active:
            raise AccountIsActiveError("Account is already active")
        self._is_active=True 
    def get_balance(self)->float:
        return self._balance

    def deposit_amount(self,amount:float):
        print("prev",self._balance)
        self._balance+=amount 
        
    def withdraw_amount(self,amount:float):
        if self._balance<amount:
            raise InsufficientBalanceInAccountError("the account has insuffucient balance")
        self._balance-=amount 
    
