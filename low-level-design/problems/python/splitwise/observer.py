from abc import ABC,abstractmethod
from expense import Expense 
class Observer(ABC):
    
    @abstractmethod 
    def on_expense_added(expense:Expense):
        pass 