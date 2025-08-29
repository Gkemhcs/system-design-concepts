from observer import Observer
from expense import Expense
class ExpenseSubject:

    def __init__(self,observers:set[Observer]=set()):
        self.__observers:set[Observer]=observers
    def add_observer(self,observer:Observer):
        self.__observers.add(observer)
    def remove_observer(self,observer:Observer):

        if observer not in self.__observers:
            raise KeyError("sorry the observer is not registered so cannot remove")
        self.__observers.remove(observer)
    def notify_on_add_expense(self,expense:Expense):
        for observer in self.__observers:
            print(f"calling {observer}")
            observer.on_expense_added(expense)