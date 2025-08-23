from observer import Observer
from transaction import Transaction
class SMSNotifier(Observer):

    def update(self, transaction: Transaction):
        print(f"Sending SMS notification for transaction: {transaction.get_transaction_id()} of type {transaction.get_transaction_type().value}  using card{transaction.get_card_number()} of total amount {transaction.get_amount()}")
