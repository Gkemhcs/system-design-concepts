from core_classes.screen import Screen
from core_classes.theatre import Theatre
from core_classes.screen_type import ScreenType
from core_classes.seat import Seat 
from core_classes.seat_type import SeatType
class TheatreService:

    def __init__(self):
        self.__screens:dict[int,Screen]={}
        self.__theatres:dict[int,Theatre]={}
        self.__screen_counter=1
        self.__theater_counter=1
        self.__seat_counter=1
    def create_theatre(self,name:str,location:str)->Theatre:
        theatre_id=self.__theater_counter
        theatre=Theatre(theatre_id,name,location)
        self.__theatres[theatre_id]=theatre 
        self.__theater_counter+=1
        print(f"theater {name} got  created successfully")
        return theatre
    def get_theatre(self,id:int)->Theatre :
        if id not in self.__theatres:
            raise Exception("sorry the theatre doesn't exist")
        else:
            return self.__theatres[id]
    def create_screen_in_theatre(self,theatre:Theatre,screen_type:ScreenType)->Screen:
        screen_id=self.__screen_counter
        screen=Screen(screen_id,screen_type,theatre)
        self.__screens[screen_id]=screen 
        theatre.add_screen(screen)
        self.__screen_counter+=1
        print(f"screen of type {screen_type.value} for created in {theatre.get_name()} successfully")
        return screen 
    def get_screen_in_theatre(self,screen_id:int)->Screen:

        if id  not in self.__screens:
            raise Exception("sorry the screen you are looking for doesn't exist")
        else:
            return self.__screens[screen_id]
    def create_seat_in_screen(self,screen_id:int,seat_type:SeatType,row:int,col:int)->Seat:
        if screen_id not in self.__screens:
            raise Exception("sorry the screen doesnt exist")
        else:
            screen=self.__screens[screen_id]
            id=self.__seat_counter
            seat=Seat(id,row,col,seat_type)
            screen.add_seats(seat)
            self.__seat_counter+=1
            print(f"seat with id {id} of type {seat_type} got created in screen screen {screen_id}")
            return seat 
    def get_seat_in_screen(self,screen_id:int,seat_id:int)->Seat:
        if screen_id not in self.__screens:
            raise Exception("sorry the screen doesnt exist")
        else:

            screen=self.__screens[screen_id]
            for seat in screen.get_seats():
                if seat.get_id()==seat_id:
                    return seat 
            return None 
    
    def get_all_seats(self,screen_id:int)->list[Seat]:

        if screen_id not in self.__screens:
            raise Exception("sorry the screen doesnt exist")
        else:
            return self.__screens[screen_id].get_seats()
    def get_all_screens_in_theatre(self,theatre_id:int)->list[Screen]:
        if theatre_id not in self.__theatres:
            raise Exception("sorry the theatre doesnt exist")
        else:
            return self.__theatres[theatre_id].get_screens()
