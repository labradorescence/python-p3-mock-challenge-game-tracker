class Game:
    def __init__(self, title):
        self.title = title
        self._results = []
        self._players = []

    # getter/setter option 1 
    # def get_title(self): # getter 
    #     return self._title # return the title property 
    # def set_title(self, title): 
    #     self._title = title 
    
    # title = property(get_title, set_title)
        
    @property 
    def title(self): #getter 
        return self._title 
    
    @title.setter #setter 
    def title(self, title):
        if isinstance(title, str) and len(title) > 0 and not hasattr(self, 'title'):
            self._title = title
        else: 
            raise Exception("Titles must be of type str/ Titles must be longer than 0 characters/ Should not be able to change after the game is instantiated")
        
    def results(self, new_result=None):
        from classes.result import Result # import result class 
        if new_result and isinstance(new_result, Result):
            if new_result not in self._results: # check if this new result is not already in the result list 
                self._results.append(new_result) # add the new result to the result list 
        return self._results # return a list of al the results associated w this game 
        pass
    
    def players(self, new_player=None): 
        from classes.player import Player
        if new_player and isinstance(new_player, Player):# if there's a new player and the new_player is a PLAYER class instance 
            self._players.append(new_player) # add the player to the players list 
        return self._players #return the players list 

        pass
    
    def average_score(self, player):
        player_scores = [ each_r. score for each_r in self._results if each_r.player == player]
        if player_scores:
            return sum(player_scores) / len(player_scores)
        return 0
        pass