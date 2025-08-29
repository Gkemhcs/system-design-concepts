from equal_split import EqualSplit
from percentage_split import PercentageSplit
from split import Split

class SplitFactory:

    @staticmethod 
    def create_split(split_type:str)->Split:

        if split_type=="equal":
            print("the split of type equal split created")
            return EqualSplit()
        elif split_type=="percentage":
            print("the split of type percentage split created")
            return PercentageSplit()
        else:
            print("the passed split not supported supported ones are equal,exact and percentage")
            raise NotImplementedError("sorry the split_type is not supported currently")
        