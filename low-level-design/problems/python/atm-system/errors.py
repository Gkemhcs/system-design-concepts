
class AccountIsActiveError(Exception):
    pass

class AccountIsInactiveError(Exception):
    pass

class InsufficientBalanceInAccountError(Exception):
    pass 

class CardBlockedError(Exception):
    pass 
class CardIsNotBlockedError(Exception):
    pass 

class AccountAlreadyExistsError(Exception):
    pass 
class AccountNotExistsError(Exception):
    pass 

class CardAlreadyExistsError(Exception):
    pass 


class CardNotExistError(Exception):
    pass 

class SufficientChangeNotAvailableError(Exception):
    pass 

class InvalidTransactionError(Exception):
    pass 

class PINMisMatchError(Exception):
    pass 

class MismatchedTransactionError(Exception):
    pass 

class InsufficientAmountInATMError(Exception):
    pass 