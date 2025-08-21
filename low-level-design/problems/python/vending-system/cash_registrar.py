
class Coin:
    FIVE = 5
    TEN = 10
    TWENTY = 20


class CashRegistrar:
    def __init__(self, cashMap: dict[Coin, int]):
        self.cashCounter: dict[Coin, int] = cashMap
    
    def add_balance(self, coin: Coin, quantity: int):
        if coin in self.cashCounter:
            self.cashCounter[coin] += quantity
        else:
            self.cashCounter[coin] = quantity
    
    def return_balance(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")
        
        # Create a copy of current cash counter to work with
        temp_counter = self.cashCounter.copy()
        remaining_amount = amount
        
        # Try to deduct coins in order: 20, 10, 5
        coins_to_deduct = [Coin.TWENTY, Coin.TEN, Coin.FIVE]
        
        for coin in coins_to_deduct:
            while remaining_amount >= coin and temp_counter.get(coin, 0) > 0:
                temp_counter[coin] -= 1
                remaining_amount -= coin
        
        # Check if we can return the full amount
        if remaining_amount == 0:
            # Update the actual cash counter
            self.cashCounter = temp_counter
            print(f"Balance returned: {amount}")
            return True
        else:
            # Cannot return the full amount, raise error
            raise ValueError("Insufficient balance")
