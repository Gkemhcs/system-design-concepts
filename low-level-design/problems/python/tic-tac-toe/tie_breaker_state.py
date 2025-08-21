from state import State 
from typing import TYPE_CHECKING
from errors import InvalidMoveError
if TYPE_CHECKING:
    from board import Board



class TieState:
    def change_state(self,Board):
         raise  InvalidMoveError("Game is already over  It's tie breaker")

    