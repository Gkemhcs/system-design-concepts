from min_transaction_strategy import MinTransactionStrategy
from user_pair import UserPair
from user import User 
from transaction import Transaction 
class SimpleMinTransactionGetter(MinTransactionStrategy):

    def __init__(self):
        pass 

    def calculate_min_transactions(self,balances:dict[UserPair,float])->int:    
        net_balances:dict[User,float]={}

        # Calculate net balance for each user
        for pair, balance in balances.items():
            net_balances[pair.get_user1()]=net_balances.get(pair.get_user1(),0.0)-balance
            net_balances[pair.get_user2()]=net_balances.get(pair.get_user2(),0.0)+balance
        
        crediters:list[User]=[]
        debiters:list[User]=[]

        # Separate users into creditors (positive balance) and debtors (negative balance)
        for user,balance in net_balances.items():
            if balance < -0.01:  # Debtor (owes money)
                debiters.append(user)
            elif balance > 0.01:  # Creditor (is owed money)
                crediters.append(user)
        
        # Sort by absolute balance values (largest first) for optimal matching
        crediters.sort(key=lambda x: net_balances[x], reverse=True)
        debiters.sort(key=lambda x: net_balances[x])  # Ascending (most negative first)
        
        transactions:list[Transaction]=[]
        
        # Use a greedy approach: match largest creditors with largest debtors
        while crediters and debiters:
            crediter = crediters[0]
            debiter = debiters[0]
            
            creditor_balance = net_balances[crediter]
            debitor_balance = net_balances[debiter]
            
            # Calculate transaction amount
            transacted_amount = min(creditor_balance, -debitor_balance)
            
            # Create transaction
            transactions.append(
                Transaction(debiter, crediter, transacted_amount)
            )
            
            # Update balances
            net_balances[crediter] -= transacted_amount
            net_balances[debiter] += transacted_amount
            
            # Remove users whose balances are settled (close to 0)
            if abs(net_balances[crediter]) < 0.01:
                crediters.pop(0)
            if abs(net_balances[debiter]) < 0.01:
                debiters.pop(0)
        print(transactions)
        return len(transactions) 
            


