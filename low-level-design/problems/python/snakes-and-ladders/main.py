from board import Board 
from game import Game 
from ladder import Ladder
from snake import Snake


def main():
        board=Board(100)
        board.set_entity(Ladder(42,93))
        board.set_entity(Snake(17, 7))
        board.set_entity(Ladder(15,26))
        board.set_entity(Snake(54,34))           
        board.set_entity(Ladder(72,84))
        board.set_entity(Snake(62,19))
        game=Game(board)
        game.add_player("Alice")
        game.add_player("Bob")
        game.play()


if __name__=="__main__":
    main()