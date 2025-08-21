from enum import Enum 

class PlayerSymbol(Enum):
    X="X"
    O="O"

class Player:
    def __init__(self,name,symbol:PlayerSymbol):

        self.symbol=symbol 
        self.name=name 


class Player1(Player):
    def __init__(self,name):
        super().__init__(name,PlayerSymbol.X)
class Player2(Player):
    def __init__(self,name):
        super().__init__(name,PlayerSymbol.O)



