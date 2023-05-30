class Player:

    all = []

    ### Initializers
    def __init__(self, username):
        self.username = username
        self._results = []
        self._games_played = []

    ### Properties
    @property #getter
    def username(self):
        return self._username #return username
    
    @username.setter #setter
    def username(self, username):
        if isinstance(username, str) and 2 <= len(username) <= 16:
            self._username = username
        else:
            raise Exception("username must be a string and length between 2 and 16.")
        

    ### Object Relationship Attributes and Properties
    def results(self, new_result=None):
        from classes.result import Result
        if new_result and isinstance(new_result, Result):
            self._results.append(new_result)
        return self._results
    
    def games_played(self, new_game=None):
        from classes.game import Game
        if new_game and isinstance(new_game, Game):
            self._games_played.append(new_game)
        return self._games_played
    

    ### Aggregate and Association Methods 
    def played_game(self, game): # if the `Player` has played this `Game` (if there is a `Result` instance that has this `Player` and `Game`), returns 'True' else `False`
        return game in self._games_played
    
    def num_times_played(self, game):
        return len([r for r in self._results if r.game == game])
    
#### Bonus: Aggregate and Association Method
    @classmethod #class method
    def highest_scored(cls, game): #cls = class 
        if cls.all:
            max_player = None
            max_score = 0
            for p in cls.all:
                if game.average_score(p) > max_score:
                    max_player = p
                    max_score = game.average_score(p)
            return max_player
        return None
        