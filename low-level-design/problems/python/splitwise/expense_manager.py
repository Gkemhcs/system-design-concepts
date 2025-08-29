from expense import Expense
from expense_subject import ExpenseSubject

class ExpenseManager:
    def __init__(self,expense_subject:ExpenseSubject):
        self.__expenses:dict[str,Expense]={}
        self._expense_subject:ExpenseSubject=expense_subject
    def add_expense(self,expense:Expense):
        self.__expenses[expense.get_id()]=expense
        self._expense_subject.notify_on_add_expense(expense)
    
    def get_all_expenses(self)->list[Expense]:
        return self.__expenses