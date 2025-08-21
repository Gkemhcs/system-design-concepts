class ProductsOutOfStockError(Exception):
    pass 

class VendingMachineOutofStock(Exception):
    pass 

class PaymentFailedError(Exception):
    pass 

class ProductNotFoundError(Exception):
    pass

class AmountNotEnoughError(Exception):
    pass    

class InvalidBalance(Exception):
    pass 