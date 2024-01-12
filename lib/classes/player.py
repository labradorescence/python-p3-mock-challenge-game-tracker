class Player:

    all = []

    def __init__(self, username):
        self.username = username
        self._results = []
        self._games_played = []

    @property #getter 
    def username(self):
        return self._username 
    @username.setter #setter 
    def username(self, username):
        if isinstance(username, str) and 2 <= len(username) <= 16: 
            self._username = username
        else: 
            raise Exception("Usernames must be of type str/Usernames must be between 2 and 16 characters, inclusive./Should be able to change after the player is instantiated")
        
    def results(self, new_result=None):
        from classes.result import Result

        if new_result and isinstance(new_result, Result):
            if new_result not in self._results:
                self._results.append(new_result)
        return self._results # return a list of all the result 
        pass
    
    def games_played(self, new_game=None):
        from classes.game import Game #import game class 
        if new_game and isinstance(new_game, Game):
            self._games_played.append(new_game) # append the new game 
        return self._games_played # return a list with all the  games 
        pass
    
    #Aggregate and Association Methods
    def played_game(self, game):
        return game in self._games_played # true or false
        pass
    
    def num_times_played(self, game):
        return len([ re for re in self._results if re.game == game])
        pass
    
    @classmethod
    def highest_scored(cls, game):
        if cls.all:
            max_player = None
            max_score = 0 
            for p in cls.all:
                if game.average_score(p) > max_score:
                    max_player = p
                    max_score = game.average_score(p)
            return max_player
        return None