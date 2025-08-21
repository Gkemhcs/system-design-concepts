from cell import Cell
from errors import CellAlreadyOccupiedError,InvalidMoveError
from player import Player
from state import State 
class Board:
    def __init__(self,rows,cols):
        self.grid=[
            [Cell(row,col) for col in range(cols)] for row in range(rows)
        ]
        self.rows=rows 
        self.cols=cols 
        self.rem_cells=rows*cols
    def canPlace(self,row,col):
        return self.grid[row][col].canPlace()
    def isValidCell(self,row,col):
       if row<0 or row>=self.rows or col<0 or col>=self.cols:
            return False 
       else:
           return True 
   
    def place(self,row,col,player:Player):
        if not self.isValidCell(row,col):
            raise InvalidMoveError("Invalid move")
        if not self.canPlace(row,col):
            raise InvalidMoveError("Invalid move")
       
        if self.grid[row][col].canPlace():
        
            self.grid[row][col].place(player)
            self.rem_cells-=1
        else:
            raise CellAlreadyOccupiedError("Cell already occupied")
    def remove(self,row,col):
        self.grid[row][col].remove()
        self.rem_cells+=1
    def getPlayer(self,row,col)->Player:
        return self.grid[row][col].getPlayer()
    def getRow(self,row)->list[int]:
        return self.grid[row]
    def getCol(self,col)->list[int]:
        return [row[col] for row in self.grid]
    def getDiagonal(self)->list[int]:
        return [self.grid[i][i] for i in range(len(self.grid))]
    def getAntiDiagonal(self)->list[int]:
        return [self.grid[i][len(self.grid)-i-1] for i in range(len(self.grid))]
    def isFull(self)->bool:
        if self.rem_cells==0:
            return True 
        else:
            return False 
    def display_board(self,):
        for row in self.grid:
            for cell in row:
                player=cell.getPlayer()
                if player==None:
                    print(".",end=" ")
                else:   
                    print(player.symbol.value,end=" ")
            print()
    def checkWinner(self,player:Player):
        for i in range(self.rows):
            if all(cell.getPlayer()==player for cell in self.getRow(i)) and player==self.getPlayer(i,0):
                return True 
        for col in range(self.cols):
            if all(cell.getPlayer()==player for cell in self.getCol(col)) and player==self.getPlayer(0,col):
                return True 
        if all(cell.getPlayer()==player for cell in self.getDiagonal()) and player==self.getPlayer(0,0):
            return True 
        if all(cell.getPlayer()==player for cell in self.getAntiDiagonal()) and player==self.getPlayer(0,self.cols-1):
            return True 
        return False 

        


        
            

