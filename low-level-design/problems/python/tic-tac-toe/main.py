from game import Game 
from player import Player1,Player2
from board import Board
from errors import InvalidMoveError,CellAlreadyOccupiedError
from player_x_won_state import PlayerXWonState
from player_y_won_state import PlayerYWonState
from tie_breaker_state import TieState

def main():

    player1=Player1("player1")
    player2=Player2("player2")
    game=Game(3,3,player1,player2)
    game.display()
    while True:
        try:
        
            print(f"Its {game.current_player.name}'s turn")
            row=int(input("Enter row:"))
            col=int(input("Enter col:"))
            game.play(row,col,game.current_player)
        
            if game.current_state==PlayerXWonState or game.current_state==PlayerYWonState or game.current_state==TieState:
                break
            game.display()
            print("----  ---")
        except InvalidMoveError as e:
            print(e)
        except CellAlreadyOccupiedError as e:
            print(e)
        except ValueError as e:
            print("Invalid input")  
        

   
   



if __name__=="__main__":
    main()
