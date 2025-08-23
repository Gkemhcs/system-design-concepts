from atm_system_singleton import ATMSystemSingleton
from card_type import CardType
from transaction_types import TransactionType
from denominations import Denomination
from sms_notifier import SMSNotifier
from invoice_generator import PaperInvoicer
def main():

    atm_system=ATMSystemSingleton.get_atm_system()
    account1=atm_system.create_account(1234,"gokul",1000.0)
    account2=atm_system.create_account(5678,"arjun",2000.0)
    
    card1=atm_system.create_card(12345,CardType.MASTERCARD,2015,account1.get_account_number())
    atm_system.register_observer(SMSNotifier())
    atm_system.register_observer(PaperInvoicer())
    atm_system.insert_card(card1)
    atm_system.authenticate_card(2015)
    atm_system.display_available_transactions()
    atm_system.select_transaction_type(TransactionType.CHECK_BALANCE)
    print(atm_system.check_balance())
    
    atm_system.add_amount(Denomination.FIVE_HUNDRED, 10)
    atm_system.add_amount(Denomination.HUNDRED, 10)
    atm_system.insert_card(card1)
    atm_system.authenticate_card(2015)
    atm_system.display_available_transactions()
    atm_system.select_transaction_type(TransactionType.WITHDRAW)
    notes=atm_system.withdraw(600)
 
    for key in notes.keys():
        print(f"denomination {key.value} count {notes[key]}")
    atm_system.insert_card(card1)
    atm_system.authenticate_card(2015)
    atm_system.display_available_transactions()
    atm_system.select_transaction_type(TransactionType.DEPOSIT)
    atm_system.deposit({Denomination.FIVE_HUNDRED:1, Denomination.HUNDRED:1})
    atm_system.insert_card(card1)
    atm_system.authenticate_card(2015)
    atm_system.display_available_transactions()
    atm_system.select_transaction_type(TransactionType.CHECK_BALANCE)
    print(atm_system.check_balance())
    

if __name__=="__main__":
    main()  