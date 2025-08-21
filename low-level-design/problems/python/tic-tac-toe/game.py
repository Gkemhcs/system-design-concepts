from board import Board 
from player import Player,PlayerSymbol
from playing_state import PlayingState
from tie_breaker_state import TieState
from player_x_won_state import PlayerXWonState
from player_y_won_state import PlayerYWonState
from errors import InvalidMoveError,CellAlreadyOccupiedError
from state import State

class Game:
    def __init__(self,rows,cols,player1:Player,player2:Player):
        self.board=Board(rows,cols)
        self.current_state=PlayingState()
        self.player1:Player=player1
        self.player2:Player=player2
        self.current_player:Player=self.player1
    def change_state(self,state:State):
        self.current_state=state
    def play(self,row,col,player):
        self.board.place(row,col,player)
        self.current_state.change_state(self,player)
        if self.current_state==PlayerXWonState or self.current_state==PlayerYWonState :
            if self.current_state==PlayerXWonState:
                print(f"Player {player.name} won")
            else:
                print(f"Player {player.name} won")
        elif  self.current_state==TieState:
            
                print("Its a tie")

        elif self.current_player==self.player1:
            self.current_player=self.player2
        else:
            self.current_player=self.player1
    def check_board_is_full(self):
        return self.board.isFull()
    def checkWinner(self,player:Player):
        return self.board.checkWinner(player)
    def display(self):
        self.board.display_board()
