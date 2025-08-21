from __future__ import annotations
from state import State

from typing import TYPE_CHECKING
from player import Player
if TYPE_CHECKING:
    from board import Board
    from game import Game
  

class PlayingState(State):
    
    def change_state(self,game:Game,player:Player):
        from player_x_won_state import PlayerXWonState
        from player_y_won_state import PlayerYWonState
        from player import PlayerSymbol 
        from tie_breaker_state import TieState
        if game.checkWinner(player):
            if player.symbol==PlayerSymbol.X:
                game.change_state(PlayerXWonState)
            else:
                game.change_state(PlayerYWonState)
        elif game.check_board_is_full():
            game.change_state(TieState)
    
