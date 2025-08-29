from observer import Observer
from min_transaction_strategy import MinTransactionStrategy
from user_pair import UserPair
from user import User 
from expense import Expense
from transaction import Transaction
class BalanceSheet(Observer):

   def __init__(self,min_transaction_strategy:MinTransactionStrategy):
        self.__balances:dict[UserPair,float]={}
        self.__strategy=min_transaction_strategy
    
   def on_expense_added(self,expense:Expense):
      
      payee=expense.get_payer()
      user_shares=expense.get_user_shares()
      for payer in expense.get_participants():
         if payer!=payee:
            user_pair=UserPair(payer,payee)
            self.__balances[user_pair]=self.__balances.get(user_pair,0)+user_shares.get(payer,0)
    
   def get_balance(self,user1:User,user2:User)->float:
       pair1=UserPair(user1,user2)
       pair2=UserPair(user2,user1)
       balance1=self.__balances.get(pair1,0.0)
       balance2=self.__balances.get(pair2,0.0)
       return   balance1-balance2

   def get_user_net_balance(self,user:User)->float:
        net_balance=0
        for user_pair in self.__balances.keys():
            if user==user_pair.get_user1():
                net_balance-=self.get_amount_by_pair(user_pair)
            elif user==user_pair.get_user2():
               net_balance+=self.get_amount_by_pair(user_pair)
        return  net_balance

   def get_amount_by_pair(self,user_pair:UserPair)->float:
       return self.__balances.get(user_pair,0.0)
    
   def get_all_user_pairs(self)->dict[UserPair,float]:
       for pair,amount in self.__balances.items():
          print(f"{pair}:- {amount}")
   def change_strategy(self,strategy:MinTransactionStrategy):
       self.__strategy=strategy
   def get_transaction_settlements(self)->float:
      return  self.__strategy.calculate_min_transactions(self.__balances)
   
   

       
   def __str__(self):
       return "Balance sheet tracker"
    