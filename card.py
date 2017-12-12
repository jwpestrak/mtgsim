# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Card(object):
    
    def __init__(self, name, color):
        self.name  = name
        self.color = color
        self.state = None
    
    def set_state(self, state):
        self.state = state
    
    def get_state(self):
        return self.state
    
class Land(Card):
    
    def __init__(self):
        pass
    
class Creature(Card):
    
    def __init__(self, cost = {"black": 0, "blue": 0, "green": 0, "red": 0, "white": 0, "colorless": 0}):
        self.cost = cost

binder = [
    Land("Forest", "green"),
    Creature("Ancient Brontodon", "green", {"black": 0, "blue": 0, "green": 2, "red": 0, "white": 0, "colorless": 6}),
]

#deck = [for card in binder #randomly select card until 40 are chosen]        