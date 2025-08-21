from player import Player
class Cell:
    def __init__(self,row,col):
        self.row=row
        self.col=col 
        self._player=None 
    def canPlace(self)->bool:
        if self._player==None:
            return True 
        else:
            return False 
    
    def place(self,player):
        self._player=player
    def getPlayer(self)->Player:
        return self._player
    def getRow(self)->int:
        return self.row
    def getCol(self)->int:
        return self.col