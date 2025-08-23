from denominations import Denomination
from errors import SufficientChangeNotAvailableError
class CashInventory:
    def __init__(self):
        self._cash_stock:dict[Denomination:int]={}
        self._total_cash:float=0
    
    def add_cash(self,cash_type:Denomination,count:int):
        if cash_type in self._cash_stock:
            self._cash_stock[cash_type]+=count 
        else:
            self._cash_stock[cash_type]=count 
        self._total_cash+=cash_type.value*count 
        
    
    def deposit_cash(self,denominations:dict[Denomination,int]):
        for denomination in denominations.keys():
            self.add_cash(denomination,denominations[denomination])
    def is_sufficient(self,amount:float)->bool:
        return self._total_cash>=amount 

    def dispense_cash(self, amount: float) -> dict[Denomination, int]:
        return_cash: dict[Denomination, int] = {}
        remaining_amount = amount
        
        # Sort denominations from highest to lowest value
        for amount_type in sorted(self._cash_stock.keys(), key=lambda x: x.value, reverse=True):
            # Check if we have this denomination and if it can be used
            if amount_type in self._cash_stock and self._cash_stock[amount_type] > 0:
                # Calculate how many notes of this denomination we can use
                notes_needed = min(remaining_amount // amount_type.value, self._cash_stock[amount_type])
                
                if notes_needed > 0:
                    return_cash[amount_type] = notes_needed
                    remaining_amount -= notes_needed * amount_type.value
                    
                    # If we've dispensed the full amount, break
                    if remaining_amount == 0:
                        break
        
        if remaining_amount == 0:
            # Successfully dispensed the amount, update inventory
            for denomination, count in return_cash.items():
                self._cash_stock[denomination] -= count
            self._total_cash -= amount
            return return_cash
        else:
            # Couldn't dispense the full amount, raise error
            raise SufficientChangeNotAvailableError("sorry the request amount doesn't have sufficient change try to enter a different amount")
    