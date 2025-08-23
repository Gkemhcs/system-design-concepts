from enum import Enum 

class TransactionType(Enum):
    WITHDRAW="withdraw"
    DEPOSIT="deposit"
    CHECK_BALANCE="check_balance"