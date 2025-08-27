from dice import Dice 
from board import Board
from game_status import GameStatus
from player import Player
from errors import GameAlreadyProgressedError,InsufficientPlayersError

class Game :

    def __init__(self,board:Board):
        self.__board=board 
        self.__players=[]
        self.__current_player=-1
        self.__dice=Dice(1,6)
        self.__winner=None 
        self.__status:GameStatus=GameStatus.NOT_STARTED
        self.__turn_count=0  # Add turn counter to prevent infinite loops
    def add_player(self,name:str):
        if self.__status==GameStatus.NOT_STARTED:
            player=Player(name)
            self.__players.append(player)
        else:
            raise GameAlreadyProgressedError("sorry the game already progressed , cannot add now")

    def reset(self):
        self.__status=GameStatus.NOT_STARTED
        self.__current_player=-1
        self.__winner=None 
        self.__turn_count=0  # Reset turn counter

    def play(self):
        
        self.reset()
        if len(self.__players)<2:
            print("Need at least two players to start the game.")
            raise InsufficientPlayersError("At least two players are required to start the game.")
            

        self.__status=GameStatus.RUNNING

        while self.__status!=GameStatus.COMPLETED:
            for player in self.__players:
                self.__current_player=player
                self.take_turn()
                if self.__winner is not None:
                    break

    def take_turn(self):
        # Safety check to prevent infinite loops
        self.__turn_count += 1
              
        player=self.__current_player
        dice_count=self.__dice.roll()
        current_position=player.get_position()
        next_position=current_position+dice_count

        if next_position==self.__board.get_size():
            player.set_position(next_position)
            self.__winner=player
            self.__status=GameStatus.COMPLETED
            print(f"Hooray! {player.get_name()} reached the final square {self.__board.get_size()} and won!")
            return 

        if next_position > self.__board.get_size():
            print(f"Oops, {player.get_name()} needs to land exactly on {self.__board.get_size()}. Turn skipped.")
            return

        final_position=self.__board.get_next_position(next_position)
        if final_position>next_position:
             print(f"Wow! {player.get_name()} found a ladder 🪜 at {next_position} and climbed to {final_position}.")
        elif final_position<next_position:
            print(f"Oh no! {player.get_name()} was bitten by a snake 🐍 at {next_position} and slid down to {final_position}.")
        else:
            print(f"{player.get_name()} moved from {current_position} to {final_position}.")

        player.set_position(final_position)
        
        # Check if player won after moving to final position
        if final_position == self.__board.get_size():
            self.__winner = player
            self.__status = GameStatus.COMPLETED
            print(f"Hooray! {player.get_name()} reached the final square {self.__board.get_size()} and won!")
            return
       
        # Extra turn for rolling a 6 (but only if game isn't over)
        if dice_count==6 and self.__status != GameStatus.COMPLETED:
            print(f"{player.get_name()} rolled a 6! Extra turn!")
            self.take_turn()
    

        

