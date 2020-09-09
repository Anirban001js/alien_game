"""
Created on Mon Sep  7 20:13:24 2020

@author: anirbandebnath
"""
class GameStats():
    """Track the statistics of the allien Invansion."""
    def __init__(self, ai_settings):
        self.ai_settings=ai_settings
        self.reset_stats()
        #game stage
        self.game_active=False
        #High Score should never be reset
        self.high_score=0
        
    def reset_stats(self):
        self.ships_left=self.ai_settings.ship_limit
        self.score=0
        self.level=1

