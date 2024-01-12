class Player:

    all = []

    def __init__(self, username):
        self.username = username
        self._results = []
        self._games_played = []

    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self, username):
        if isinstance(username, str) and 2 <= len(username) <= 16:
            self._username = username
        else:
            raise Exception("username must be a string and length between 2 and 16.")
        
    def results(self, new_result=None):
        from classes.result import Result #import result class

        #if there is a new_result argument
        if new_result and isinstance(new_result, Result):
            #check if the new result is not already in the list 
            if new_result not in self._results:
                self._results.append(new_result) ##add new result 
        return self._results #return a list of result associated w the player 
        pass
    
    def games_played(self, new_game=None):
        from classes.game import Game
        if new_game and isinstance(new_game, Game): 
            self._games_played.append(new_game)
        return self._games_played
        pass
    
    def played_game(self, game):
        return game in self._games_played
        pass
    
    def num_times_played(self, game):
        return len([r for r in self._results if r.game==game])
        pass
    
    @classmethod
    def highest_scored(cls, game):
        pass
        
