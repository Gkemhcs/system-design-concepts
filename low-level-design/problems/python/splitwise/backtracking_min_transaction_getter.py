from min_transaction_strategy import MinTransactionStrategy
from user_pair import UserPair
from user import User 
from transaction import Transaction
from typing import List, Tuple
import copy

class BacktrackingMinTransactionGetter(MinTransactionStrategy):
    
    def __init__(self):
        pass
    
    def calculate_min_transactions(self, balances: dict[UserPair, float]) -> list[Transaction]:
        """
        Calculate minimum number of transactions to settle debts between users.
        
        Args:
            balances: Dictionary with UserPair keys and amount values
            
        Returns:
            list[Transaction]: List of transactions needed to settle all debts
        """
        # Step 1: Calculate net balances for each user
        net_balances = self._calculate_net_balances(balances)
        
        # Create list of non-zero balances
        credit_list = []
        for user, balance in net_balances.items():
            if abs(balance) > 0.001:  # Ignore near-zero balances
                credit_list.append(balance)
        
        n = len(credit_list)  # Total number of users with non-zero balance
        
        # Get minimum transaction count
        min_transactions = self._sub_optimal_dfs(0, credit_list, n)
        
        # For now, return empty list since we're only counting transactions
        # TODO: Extend to return actual transaction objects
        return []
    
    def get_min_transaction_count(self, balances: dict[UserPair, float]) -> int:
        """
        Get only the count of minimum transactions needed.
        
        Args:
            balances: Dictionary with UserPair keys and amount values
            
        Returns:
            int: Minimum number of transactions required
        """
        # Step 1: Calculate net balances for each user
        net_balances = self._calculate_net_balances(balances)
        
        # Create list of non-zero balances
        credit_list = []
        for user, balance in net_balances.items():
            if abs(balance) > 0.001:  # Ignore near-zero balances
                credit_list.append(balance)
        
        n = len(credit_list)  # Total number of users with non-zero balance
        
        # Return minimum transaction count
        return self._sub_optimal_dfs(0, credit_list, n)
    
    def _sub_optimal_dfs(self, current_user_index: int, credit_list: List[float], n: int) -> int:
        """
        Recursively find minimum transactions required to settle debts.
        
        Args:
            current_user_index: Index of user whose balance needs settlement
            credit_list: List of net balances for all users
            n: Number of users with non-zero balances
            
        Returns:
            int: Minimum transactions required
        """
        # Skip already settled users (those with zero balance)
        while current_user_index < n and credit_list[current_user_index] == 0:
            current_user_index += 1
        
        # Base case: If all users have zero balance, no further transactions needed
        if current_user_index == n:
            return 0
        
        cost = float('inf')  # Variable to track minimum number of transactions
        
        # Try to settle currentUserBalance with a future user having opposite balance
        for next_index in range(current_user_index + 1, n):
            # Ensure we only settle debts between users with opposite balances
            if credit_list[next_index] * credit_list[current_user_index] < 0:
                # Transfer current user's balance to the next valid user
                credit_list[next_index] += credit_list[current_user_index]
                
                # Recursively settle the remaining balances
                cost = min(cost, 1 + self._sub_optimal_dfs(current_user_index + 1, credit_list, n))
                
                # Backtrack: Undo the transaction to explore other possibilities
                credit_list[next_index] -= credit_list[current_user_index]
        
        return cost
    
    def _calculate_net_balances(self, balances: dict[UserPair, float]) -> dict[User, float]:
        """Calculate net balance for each user from pair-wise balances."""
        net_balances = {}
        
        for pair, balance in balances.items():
            user1 = pair.get_user1()
            user2 = pair.get_user2()
            
            net_balances[user1] = net_balances.get(user1, 0.0) - balance
            net_balances[user2] = net_balances.get(user2, 0.0) + balance
        
        return net_balances
