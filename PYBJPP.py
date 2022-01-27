# This project is the personal project; Black Jack project first created on Jan 18, 2022.

def _APPINFO() : # Contains the infomation about this application.
    _INFO = {"developer" : "Mr.Snowman", "version" : "0.111", "build" : "20220127", "appCode" : "PYBJPP"} # build format: YYYYMMDD
    return _INFO

from re import S
from pybjpp_database import *

class Deck :
    faceCards = ['King', 'Queen', 'Jack']
    specialCard = 'Ace'
    numberCards = Card.number_card
    
    def __init__(self, f, s, n) :
        self.faceCards = f
        self.specialCard = s
        self.numberCards = n

    def __str__(self) -> str:
        return "You have" + self.faceCards

test = Deck('K', 'A', 2)
print(Deck.specialCard)
print(test.__str__())
