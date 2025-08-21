from state import State 
from errors import InvalidMoveError
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from board import Board



class PlayerYWonState:
    def change_state(self,Board):
         raise  InvalidMoveError("Game is already over player Y won")



