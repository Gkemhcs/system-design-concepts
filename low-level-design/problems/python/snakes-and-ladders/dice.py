from random import randint 
class Dice:
    def __init__(self, min_num: int = 1, max_num: int = 6):
        self.__min_num = min_num
        self.__max_num = max_num

    def roll(self) -> int:
        return randint(self.__min_num, self.__max_num)
    
