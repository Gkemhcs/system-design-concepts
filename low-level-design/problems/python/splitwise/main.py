from split_factory import SplitFactory
from balance_sheet import BalanceSheet
from expense_subject import ExpenseSubject
from expense import Expense 
from expense_manager import ExpenseManager
from user_manager import UserManager
from split_types import SplitType
from backtracking_min_transaction_getter import BacktrackingMinTransactionGetter
from simple_min_transaction_getter import SimpleMinTransactionGetter

def main():
    user_manager=UserManager()
    koti=user_manager.create_user("user-1","koti","gudi@gmail",9093093093)
    eswar=user_manager.create_user("user-2","eswar","eswar@gmail",9309303003)
    mani=user_manager.create_user("user-3","mani","mani@gmail",9002002090)

    equal_split=SplitFactory.create_split("equal")
    participants=[koti,eswar,mani]
    shares1=equal_split.split(participants,300,{})
    expense1=Expense("expense-1","room rent",koti,300.0,participants,shares1)
    
    percentage_split=SplitFactory.create_split("percentage")

    shares2=percentage_split.split(participants,1000,{koti:60,eswar:20,mani:20})
    expense2=Expense("expense-2","online shopping",mani,1000,participants,shares2,SplitType.PERCENT)


    backtracking_transaction_getter=BacktrackingMinTransactionGetter()
    simple_transaction_getter=SimpleMinTransactionGetter()
    balance_sheet=BalanceSheet(simple_transaction_getter)
    expense_subject=ExpenseSubject()
    expense_subject.add_observer(balance_sheet)
    expense_manager=ExpenseManager(expense_subject)
    expense_manager.add_expense(expense1)
    expense_manager.add_expense(expense2)

    balance_sheet.get_all_user_pairs()
    print(balance_sheet.get_user_net_balance(eswar))
    print(balance_sheet.get_user_net_balance(koti))
    print(balance_sheet.get_user_net_balance(mani))


    count=balance_sheet.get_transaction_settlements()
    print(f"Total transactions using simple strategy: {count}")
    balance_sheet.change_strategy(backtracking_transaction_getter)
    count=balance_sheet.get_transaction_settlements()
    
    print(f"Total transactions using backtracking strategy: {count}")

if __name__=="__main__":
    main()