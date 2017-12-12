# -*- coding: utf-8 -*-
"""
This is a module that contains Classes used for simulating draw of a hand from
a deck of Magic: The Gathering cards.

Currently, in addition to a Card superclass, there are only two usable 
subclasses - Creature and Land.
"""

# Define classes

class Card(object):
    
    def __init__(self, name, color):
        self.name   = name
        self.color  = color
        self.state  = None # values can be 'In Hand', 'On Battlefield', 'In Graveyard', 'Exiled'
        self.tapped = False
        
    def set_state(self, state):
        self.state = state
    
    def get_state(self):
        return self.state
    
    def tap(self):
        self.tapped = True
        
    def untap(self):
        self.tapped = False
    
class Land(Card):
    
    def __init__(self):
        pass
            
class Creature(Card):
    
    def __init__(self, cost = {"black": 0, "blue": 0, "green": 0, "red": 0, "white": 0, "colorless": 0}):
        self.cost = cost

class Instant(Card):
    
    def __init__(self):
        self.tapped = None

# main 

# populate binder
binder = [
    Land("Forest", "green"),
    Creature("Ancient Brontodon", "green", {"black": 0, "blue": 0, "green": 2, "red": 0, "white": 0, "colorless": 6}),
]

# populate (and shuffle) deck

#deck = [for card in binder #randomly select card until 40 are chosen]        

# draw seven card hand

hand = []

if __name__ == "__main__":
    pass